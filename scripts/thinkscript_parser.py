from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import argparse
import json
import re
from typing import List, Optional


# ----------------------------
# Models
# ----------------------------

@dataclass
class ParseIssue:
    severity: str  # error | warning | info
    rule: str
    message: str
    line: Optional[int] = None


@dataclass
class StatementNode:
    kind: str
    text: str
    line: int
    identifier: Optional[str] = None
    calls: List[str] = field(default_factory=list)


@dataclass
class ParseResult:
    statements: List[StatementNode] = field(default_factory=list)
    issues: List[ParseIssue] = field(default_factory=list)

    @property
    def has_errors(self) -> bool:
        return any(i.severity == "error" for i in self.issues)


# ----------------------------
# Parser
# ----------------------------

class ThinkScriptParser:
    """
    Minimal structural parser (not full grammar):
    - splits statements safely by semicolon
    - classifies common declaration/call patterns
    - emits deterministic structural issues
    """

    _call_re = re.compile(r"\b([A-Za-z_]\w*)\s*\(")
    _decl_re = re.compile(r"^\s*(input|def|plot|rec|declare)\b", re.IGNORECASE)
    _id_after_decl_re = re.compile(
        r"^\s*(input|def|plot|rec)\s+([A-Za-z_]\w*)", re.IGNORECASE
    )

    def parse(self, source: str) -> ParseResult:
        result = ParseResult()
        cleaned = self._strip_comments(source)
        statements, trailing = self._split_statements(cleaned)

        for stmt_text, line in statements:
            node = self._classify(stmt_text, line)
            result.statements.append(node)

        # trailing non-empty text means probable missing semicolon
        if trailing.strip():
            result.issues.append(
                ParseIssue(
                    severity="error",
                    rule="T1",
                    message="Possible missing semicolon at end of script.",
                    line=self._line_for_offset(cleaned, len(cleaned) - len(trailing)),
                )
            )

        # deterministic checks from hook policy
        self._run_rule_checks(source=source, cleaned=cleaned, parsed=result)

        return result

    def _strip_comments(self, source: str) -> str:
        out_lines = []
        for line in source.splitlines():
            # thinkScript supports '#' comments and '//' style in many examples
            line_no_hash = re.sub(r"#.*$", "", line)
            line_no_slash = re.sub(r"//.*$", "", line_no_hash)
            out_lines.append(line_no_slash)
        return "\n".join(out_lines)

    def _split_statements(self, source: str):
        statements = []
        buf = []
        line = 1
        stmt_start_line = 1
        depth = 0
        in_string = False
        quote_char = ""

        for ch in source:
            if ch == "\n":
                line += 1

            if in_string:
                buf.append(ch)
                if ch == quote_char:
                    in_string = False
                continue

            if ch in ("'", '"'):
                in_string = True
                quote_char = ch
                buf.append(ch)
                continue

            if ch == "(":
                depth += 1
                buf.append(ch)
                continue

            if ch == ")":
                depth = max(0, depth - 1)
                buf.append(ch)
                continue

            if ch == ";" and depth == 0:
                text = "".join(buf).strip()
                if text:
                    statements.append((text, stmt_start_line))
                buf = []
                stmt_start_line = line
                continue

            if not buf and ch == "\n":
                stmt_start_line = line
            buf.append(ch)

        trailing = "".join(buf)
        return statements, trailing

    def _classify(self, stmt_text: str, line: int) -> StatementNode:
        kind = "expression"
        identifier = None

        decl = self._decl_re.search(stmt_text)
        if decl:
            kind = decl.group(1).lower()

        m = self._id_after_decl_re.search(stmt_text)
        if m:
            identifier = m.group(2)

        calls = [m.group(1) for m in self._call_re.finditer(stmt_text)]
        return StatementNode(kind=kind, text=stmt_text, line=line, identifier=identifier, calls=calls)

    def _run_rule_checks(self, source: str, cleaned: str, parsed: ParseResult) -> None:
        # Use cleaned (comment-stripped) text for content checks so that
        # comments starting with '#' never trigger false positives.
        text = cleaned

        # G1 empty
        if not text.strip():
            parsed.issues.append(ParseIssue("error", "G1", "Output is empty.", 1))

        # G2 placeholders (checked against comment-stripped source)
        if re.search(r"(?i)\{\{.*?\}\}|\.{3}existing code\.{3}|\bTODO\b|<insert[^>]*>", text):
            parsed.issues.append(ParseIssue("error", "G2", "Placeholder content detected."))

        # T4 invalid historical indexing on ask/bid (checked against comment-stripped source)
        if re.search(r"(?i)\bask\s*\[", text):
            parsed.issues.append(ParseIssue("error", "T4", "Invalid historical indexing on ask."))
        if re.search(r"(?i)\bbid\s*\[", text):
            parsed.issues.append(ParseIssue("error", "T4", "Invalid historical indexing on bid."))

        # T3 @Date annotation sanity (checked against original source since @Date is a real annotation)
        if re.search(r"(?m)^\s*@Date\b", source):
            if not re.search(r"(?ms)@Date\s*\n\s*input\s+[A-Za-z_]\w*\s*=\s*\d+", text):
                parsed.issues.append(ParseIssue("error", "T3", "@Date must annotate an integer input."))

        # study/strategy structural signals
        has_plot = any(s.kind == "plot" for s in parsed.statements)
        has_add_order = any("AddOrder" in s.calls for s in parsed.statements)

        if has_add_order and not has_plot:
            parsed.issues.append(ParseIssue("warning", "T2", "Strategy detected (AddOrder) with no plot."))

    def _line_for_offset(self, text: str, offset: int) -> int:
        return text[:offset].count("\n") + 1


# ----------------------------
# CLI
# ----------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="Minimal ThinkScript parser/linter.")
    ap.add_argument("file", type=Path, help="Path to thinkScript source file")
    ap.add_argument("--json", action="store_true", help="Print JSON output")
    args = ap.parse_args()

    source = args.file.read_text(encoding="utf-8")
    parser = ThinkScriptParser()
    result = parser.parse(source)

    if args.json:
        print(
            json.dumps(
                {
                    "statements": [
                        {
                            "kind": s.kind,
                            "line": s.line,
                            "identifier": s.identifier,
                            "calls": s.calls,
                            "text": s.text,
                        }
                        for s in result.statements
                    ],
                    "issues": [i.__dict__ for i in result.issues],
                    "has_errors": result.has_errors,
                },
                indent=2,
            )
        )
    else:
        print(f"Statements: {len(result.statements)}")
        for s in result.statements:
            print(f"- line {s.line}: {s.kind} ({s.identifier or '-'}) calls={s.calls}")
        if result.issues:
            print("\nIssues:")
            for i in result.issues:
                loc = f" line {i.line}" if i.line else ""
                print(f"[{i.severity.upper()}] {i.rule}{loc}: {i.message}")
        else:
            print("\nNo issues found.")

    return 1 if result.has_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())