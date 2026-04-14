# ThinkScript Hook Policy

## Purpose

This policy defines a **minimal deterministic enforcement layer** for ThinkScript-related LLM output.

It is intended to catch:
- structurally invalid output,
- prompt-contract violations,
- and common ThinkScript convention errors that should not be left to model judgment.

This policy is intentionally narrow. It should only enforce rules that are:
1. easy to verify,
2. consistently required,
3. and safe to fail on.

---

## Enforcement Modes

### Local / interactive use
- Default to **warning-only**
- Do not block normal authoring flow

### Automated / CI use
- Treat **contract violations as failures**
- Reject artifacts that do not satisfy required format or minimum ThinkScript rules

---

## Global Output Rules

These rules apply to all prompt outputs.

### G1. Output must not be empty
- Fail if output is blank or whitespace only

### G2. No placeholder content
- Fail if output contains unresolved placeholders such as:
  - `{{...}}`
  - `<insert ...>`
  - `TODO`
  - `...existing code...`

### G3. No contradictory sections
- Fail if output mixes incompatible modes, such as:
  - validation findings plus replacement code in a validation-only response
  - explanation-only output with strategy code when code was not requested

### G4. Markdown structure must be valid
- Required headings for a prompt type must exist exactly once unless explicitly allowed otherwise

---

## Prompt-Specific Contracts

## 1. Generate Prompt Contract

### Required
- exactly **one** ThinkScript code block
- code block must be labeled `thinkscript`
- no second replacement code block

### Allowed
- short assumptions section
- short explanation section

### Fail if
- no ThinkScript block exists
- multiple competing code blocks exist
- code is obviously partial or placeholder-filled

---

## 2. Debug Prompt Contract

### Required
- corrected ThinkScript code
- root-cause list

### Allowed
- short explanation of fixes

### Fail if
- no corrected code is present
- no root-cause section is present
- response only describes problems without a usable corrected script

---

## 3. Explain Prompt Contract

### Required
- explanation content only
- no replacement code unless explicitly requested

### Fail if
- explanation is replaced by a rewritten script
- response omits semantic explanation of the script

---

## 4. Validate Prompt Contract

### Required
- `Validation Result`
- `Findings`
- `Constraint Check`
- `Summary`

### Hard rule
- **must not generate replacement code**

### Fail if
- any ThinkScript code block is returned
- output omits status or findings structure
- fix guidance contains rewritten code instead of minimal instructions

---

## 5. Strategy Conversion Prompt Contract

### Required
- `Assumptions`
- `ThinkScript Strategy`
- `Mapping (Rule → Code)`
- `Validation Checklist`

### Required code rule
- exactly one `thinkscript` code block

### Fail if
- no strategy code is present
- entries/exits are not represented
- required sections are missing

---

## Deterministic ThinkScript Rules

These checks should be enforced only when output includes ThinkScript code.

## T1. Statement termination
- Each non-block ThinkScript statement should end with `;`
- Fail on obvious missing semicolons

## T2. Strategy vs study separation
- If `AddOrder(` is present, classify as strategy output
- If prompt requires a study-only result, fail on `AddOrder(`
- If strategy conversion is requested, require `AddOrder(` or explicit strategy entry/exit logic

## T3. Valid date annotation usage
- If `@Date` is used, it must annotate an integer input
- Fail if `@Date` appears without a following `input`

## T4. No historical indexing on quote-only functions
- Fail on obvious invalid patterns such as:
  - `ask[`
  - `bid[`

## T5. Price type restrictions warning
- Warn when `ASK`, `BID`, or `MARK` are used without any note that non-Forex support is limited on intraday windows
- Do not hard-fail unless a stricter profile is enabled

## T6. Secondary aggregation sanity
- Warn if multiple secondary aggregations are mixed inside one expression without separation into variables
- Do not hard-fail unless parser support is added

## T7. Boolean painting strategy sanity
- Warn if a plot clearly intended as boolean uses a conflicting style
- Do not hard-fail

## T8. Plot presence for studies
- Study generation should contain at least one `plot`
- Fail if a study response has no `plot` and no documented reason

## T9. Declare placement
- If a `declare` statement exists, it should appear near the top of the script
- Warn if not

## T10. No unresolved recursive references
- Warn on obvious recursive definitions lacking initialization where `CompoundValue` would normally be expected
- Do not hard-fail without parser support

---

## Severity Model

### Error
Fail immediately in CI.
Examples:
- missing required section
- validation prompt emitted code
- no ThinkScript block for generation
- obvious invalid `ask[1]` / `bid[1]`

### Warning
Allow output, but flag for review.
Examples:
- secondary aggregation context risk
- unsupported price-type assumptions
- declare placement issues

### Info
Non-blocking notes only.

---

## Recommended Initial Hook Set

Start with only these enforced checks:

1. non-empty output
2. no unresolved placeholders
3. required prompt sections present
4. validation prompt emits no code
5. generation/strategy prompts contain exactly one `thinkscript` block
6. obvious `ask[` / `bid[` misuse fails
7. study outputs contain at least one `plot`
8. strategy outputs contain `AddOrder(`

This keeps enforcement minimal and predictable.

---

## Out of Scope for Initial Hooks

Do **not** attempt to deterministically enforce:
- full ThinkScript parsing
- semantic trading correctness
- profitability
- repaint detection in all cases
- platform/runtime availability of every function
- advanced aggregation-context inference

These should remain model- or reviewer-level checks unless a dedicated parser is added.

---

## Success Criteria

The hook policy is successful if it:
- blocks malformed prompt output,
- prevents validation prompts from generating code,
- catches the most common ThinkScript structural mistakes,
- and remains small enough to maintain.

---

## Suggested Implementation

- Store prompt-specific contracts as simple rule maps
- Implement the first validator as a lightweight PowerShell script
- Run warning-only locally
- Run fail-on-error in CI

## Deterministic Enforcement Runtime

Use local parser tooling as the enforcement layer:

1. Build manifest from local ThinkScript docs:
   - `scripts/build_thinkscript_manifest.py`
2. Parse/lint output:
   - `scripts/thinkscript_parser.py`
3. Run unified self-check:
   - `scripts/self-check-thinkscript.ps1`

### Required command (Windows)

```powershell
.\scripts\self-check-thinkscript.ps1 -SourcePath <path-to-thinkscript-file> -TaskType <generate|debug|strategy|study> -Mode <warn|fail>
```

### Enforcement behavior

- `warn` mode: report issues, allow output
- `fail` mode: block output/publication on `error` findings

For automated workflows and CI-generated artifacts, use `-Mode fail`.

---

## Automatic Enforcement (No End-User Action)

Deterministic enforcement is applied by the agent at runtime using:
- `scripts/validate-thinkscript-output.ps1`
- `scripts/self-check-thinkscript.ps1`
- `scripts/thinkscript_parser.py` (with manifest from `scripts/build_thinkscript_manifest.py`)

The agent runs these checks before returning ThinkScript code.
No end-user action is required.

---

## Success Criteria

The hook policy is successful if it:
- blocks malformed prompt output,
- prevents validation prompts from generating code,
- catches the most common ThinkScript structural mistakes,
- and remains small enough to maintain.

---

## Suggested Implementation

- Store prompt-specific contracts as simple rule maps
- Implement the first validator as a lightweight PowerShell script
- Run warning-only locally
- Run fail-on-error in CI

## Deterministic Enforcement Runtime

Use local parser tooling as the enforcement layer:

1. Build manifest from local ThinkScript docs:
   - `scripts/build_thinkscript_manifest.py`
2. Parse/lint output:
   - `scripts/thinkscript_parser.py`
3. Run unified self-check:
   - `scripts/self-check-thinkscript.ps1`

### Required command (Windows)

```powershell
.\scripts\self-check-thinkscript.ps1 -SourcePath <path-to-thinkscript-file> -TaskType <generate|debug|strategy|study> -Mode <warn|fail>
```

### Enforcement behavior

- `warn` mode: report issues, allow output
- `fail` mode: block output/publication on `error` findings

For automated workflows and CI-generated artifacts, use `-Mode fail`.

---

## Automatic Enforcement (No End-User Action)

Deterministic enforcement is applied by the agent at runtime using:
- `scripts/validate-thinkscript-output.ps1`
- `scripts/self-check-thinkscript.ps1`
- `scripts/thinkscript_parser.py` (with manifest from `scripts/build_thinkscript_manifest.py`)

The agent runs these checks before returning ThinkScript code.
No end-user action is required.

---

## Success Criteria

The hook policy is successful if it:
- blocks malformed prompt output,
- prevents validation prompts from generating code,
- catches the most common ThinkScript structural mistakes,
- and remains small enough to maintain.

---