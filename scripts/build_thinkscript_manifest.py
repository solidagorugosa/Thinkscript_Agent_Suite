from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

RESERVED_WORDS = {
    "above","ago","and","bar","bars","below","between","case","crosses","declare","def","default","do",
    "else","equal","equals","false","fold","from","greater","if","input","is","less","no","not","or",
    "plot","profile","rec","reference","script","switch","than","then","to","true","while","with","within","yes"
}

def build_manifest(doc_text: str) -> dict:
    functions = set()
    constants = set()
    declarations = set()
    annotations = set()

    # Function signatures like: AddLabel ( ... );
    for m in re.finditer(r"(?m)^([A-Za-z_]\w*)\s*\(", doc_text):
        name = m.group(1)
        if name.lower() not in RESERVED_WORDS and len(name) > 1:
            functions.add(name)

    # Constants like AggregationPeriod.DAY
    for m in re.finditer(r"\b([A-Za-z_]\w*\.[A-Z0-9_]+)\b", doc_text):
        constants.add(m.group(1))

    # Declarations like declare lower;
    for m in re.finditer(r"(?mi)\bdeclare\s+([a-z_]+)\s*;", doc_text):
        declarations.add(m.group(1).lower())

    # Annotations like @Date
    for m in re.finditer(r"(?m)^\s*(@[A-Za-z_]\w*)\b", doc_text):
        annotations.add(m.group(1))

    # Always include common built-in calls used as methods/flow
    functions.update({
        "AddOrder","AddLabel","AddCloud","AddChartBubble","AddVerticalLine",
        "AssignPriceColor","AssignBackgroundColor","AssignValueColor","Alert",
        "Average","ExpAverage","WMA","WildersAverage","MovingAverage",
        "Highest","Lowest","HighestAll","LowestAll","Crosses","CompoundValue"
    })

    return {
        "functions": sorted(functions),
        "constants": sorted(constants),
        "declarations": sorted(declarations),
        "annotations": sorted(annotations),
        "reserved_words": sorted(RESERVED_WORDS),
    }

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--doc", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    text = args.doc.read_text(encoding="utf-8", errors="ignore")
    manifest = build_manifest(text)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Wrote {args.out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())