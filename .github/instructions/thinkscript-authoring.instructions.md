---
description: "Use when writing, fixing, or reviewing thinkScript studies/strategies, including indicator logic, AddOrder strategies, and chart styling code."
name: "ThinkScript Authoring Rules"
---
# ThinkScript Authoring Rules

Follow these rules when generating or editing thinkScript.

## Core syntax
- End every statement with `;`.
- Use `#` for comments.
- Use `def` for intermediate values, `plot` for visible outputs, and `input` for user parameters.
- Prefer named arguments for optional parameters in long function calls.
- Use historical references with bracket syntax like `value[1]`.
- Use if-expression style for non-double branches, e.g. `AssignPriceColor(if cond then Color.GREEN else Color.RED);`.

## Type and expression safety
- Treat `Double.NaN` explicitly when a value should be hidden or invalid.
- For recursive logic, initialize with `CompoundValue` instead of relying on implicit initialization.
- Avoid invalid historical references on real-time quote functions (`ask`, `bid`).

## Platform constraints to respect
- Aggregation period used in data requests must not be lower than chart aggregation.
- For non-Forex symbols, `ASK`, `BID`, and `MARK` are only valid on intraday charts up to 15 days.
- `AssignPriceColor` cannot color the same bar from multiple studies.
- Some Boolean-function consumers (such as `SetHiding` and certain `AddLabel`/`Alert` function-input cases) evaluate only the last real bar value.

## Output quality expectations
- If the user asks for a study, include at least one `plot`.
- If the user asks for a strategy, use `AddOrder` with clear order type and entry/exit conditions.
- Keep code idiomatic and compact; avoid unnecessary variables.
- After producing code, run a short self-check: syntax terminators, declared identifiers, and platform constraints above.

## Deterministic Parser Compliance

ThinkScript code outputs are validated by the agent using:
- `scripts/self-check-thinkscript.ps1`
- `scripts/validate-thinkscript-output.ps1`
- `scripts/thinkscript_parser.py`
- `scripts/build_thinkscript_manifest.py`

In agent mode, the agent runs these directly.
In chat mode, the agent applies the inline self-validation checklist.

No end-user action is required.

Runtime command (Windows):

```powershell
.\scripts\self-check-thinkscript.ps1 -SourcePath <temp-file> -TaskType <mapped-task-type> -Mode warn
```

If parser reports `error`:
- revise and re-check once before returning code.

For automation/CI contexts, use `-Mode fail`.

## References

Follow the reference priority defined in:
- [SKILL.md](../skills/thinkscript-authoring/SKILL.md)

## Reference Usage

When answering a ThinkScript task, use the local references in this order:

1. Domain-specific reference indexes under references
2. `.github/skills/thinkscript-authoring/references/Thinkscript-Documentation-Scrape/Thinkscript_Documentation_Condensed.md`
3. `.github/skills/thinkscript-authoring/references/Thinkscript-Documentation-Scrape/thinkscript_documentation_cleaned.md`

If the first source is insufficient, fall back to the next source before inferring unsupported syntax, unavailable functions, or platform behavior.

## Hook Policy

The hook policy in `../../docs/hook-policy.md` is the deterministic output contract for ThinkScript tasks.

### Required behavior
- Follow the prompt-specific contract before returning output.
- Do not emit placeholder text.
- Do not omit required sections.
- Do not generate code in validation-only workflows.
- If generating a study, include at least one `plot` unless the task explicitly justifies otherwise.
- If generating a strategy, include explicit strategy logic such as `AddOrder()`.

### Self-check before final output
- Verify required headings
- Verify allowed/forbidden code usage
- Verify output is complete and non-empty
- Verify obvious ThinkScript convention errors are avoided

## Hook Policy Compliance

Follow the deterministic enforcement rules in `../../docs/hook-policy.md`.

Before returning ThinkScript output:
1. Check the prompt-specific contract.
2. Verify required sections are present.
3. Verify code is allowed or forbidden for the task.
4. Verify basic ThinkScript structural rules if code is included.
5. If errors exist, revise once before returning.

## Self-Validation (Required Before Returning Code)

Before returning any ThinkScript code, apply these checks inline.
These mirror the deterministic rules enforced by CI via `scripts/thinkscript_parser.py`.

### Structural checks
- [ ] Every statement ends with `;`
- [ ] Parentheses are balanced
- [ ] Braces are balanced
- [ ] No unresolved placeholders (`{{...}}`, `TODO`, `<insert>`)
- [ ] Output is not empty

### ThinkScript convention checks
- [ ] `ask[]` and `bid[]` historical indexing is never used
- [ ] `@Date` only annotates an integer input in `YYYYMMDD` format
- [ ] `declare` appears near the top of the script if used
- [ ] Study output contains at least one `plot`
- [ ] Strategy output contains at least one `AddOrder()`
- [ ] No `AddOrder()` in study-only output
- [ ] Function names match known ThinkScript functions from local references
- [ ] Constants use valid enum families (`AggregationPeriod.`, `Color.`, `OrderType.`, etc.)

### Prompt contract checks
- [ ] Generate: exactly one `thinkscript` code block
- [ ] Debug: corrected code plus root-cause list
- [ ] Explain: no replacement code unless explicitly requested
- [ ] Validate: no code blocks at all; findings only
- [ ] Strategy conversion: Assumptions, code, mapping, and checklist sections present

### On failure
- Revise output once before returning
- If unresolvable, state the issue explicitly instead of returning broken code

### CI enforcement
These same rules are enforced automatically on push/PR by:
- `.github/workflows/thinkscript-self-check.yml`
- `scripts/ci-validate.ps1` → `validate-thinkscript-output.ps1` → `self-check-thinkscript.ps1` → `thinkscript_parser.py`

No end-user action is required for CI checks.
