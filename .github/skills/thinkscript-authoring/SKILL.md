---
name: thinkscript-authoring
description: "Generate, debug, and explain thinkScript studies and strategies using local thinkScript references. Use for syntax-correct indicators, AddOrder strategies, and function-level troubleshooting."
argument-hint: "Describe the indicator/strategy goal, inputs, and chart timeframe"
user-invocable: true
---

# ThinkScript Authoring Skill

## When to use
- Creating new thinkScript indicators or strategies from natural language.
- Fixing compile/runtime issues in existing thinkScript code.
- Refactoring logic for readability while preserving behavior.
- Explaining what a thinkScript script does and where it may fail.

## Reference Priority

Use references in this order:

1. Domain indexes in `references/`
2. Condensed fallback reference:
   - `references/Thinkscript-Documentation-Scrape/Thinkscript_Documentation_Condensed.md`
3. Full fallback reference:
   - `references/Thinkscript-Documentation-Scrape/thinkscript_documentation_cleaned.md`

## Local references
- [Condensed reference](./references/Thinkscript-Documentation-Scrape/Thinkscript_Documentation_Condensed.md)
- [Full cleaned scrape](./references/Thinkscript-Documentation-Scrape/thinkscript_documentation_cleaned.md)
- [Math index](./references/math-functions.md)
- [Date/time index](./references/datetime-functions.md)
- [Profile index](./references/profile-functions.md)
- [Options index](./references/options-functions.md)
- [Portfolio index](./references/portfolio-functions.md)

If domain indexes are insufficient, use condensed fallback first, then full cleaned scrape.

## Procedure
1. Determine task type:
   - `study`: visual indicators, labels, clouds, chart styling.
   - `strategy`: uses `AddOrder`, order types, and entry/exit conditions.
   - `debug`: diagnose syntax, type, aggregation, and API misuse.
2. Gather constraints from request:
   - timeframe/aggregation assumptions
   - required plots, labels, arrows, or alerts
   - inputs and defaults
   - restrictions (for example: no repainting)
3. Map requirements to documented primitives:
   - validate function names, constants, and argument rules against references
   - check pitfalls (history indexing, unsupported price types, missing semicolons, invalid color conditionals)
4. Produce code:
   - keep code minimal and readable
   - prefer `def` building blocks and one clear `plot`/signal section
   - for strategy logic, provide explicit `AddOrder` calls and signal definitions
5. Self-validate:
   - apply the self-validation checklist before returning output
6. Return result:
   - concise explanation of intent and key lines
   - assumptions and tunable `input` values

## Output contract
- If asked to generate code: return a single complete thinkScript block.
- If asked to debug: return corrected code plus a short list of root causes.
- If docs are ambiguous: state uncertainty and propose the safest documented alternative.

## Routing Guidance
- Use `thinkscript-generate.prompt.md` for fresh indicators/studies.
- Use `thinkscript-debug.prompt.md` for fault isolation and correction.
- Use `thinkscript-explain.prompt.md` for line-by-line semantics.
- Use `thinkscript-validate.prompt.md` for constraint checks only (no code generation).
- Use `thinkscript-strategy-convert.prompt.md` for plain-English strategy conversion.

## Hook Policy

Follow compliance rules in:
- [thinkscript-authoring.instructions.md](../../instructions/thinkscript-authoring.instructions.md)

## Self-Validation

Before returning ThinkScript code, apply the self-validation checklist in:
- [thinkscript-authoring.instructions.md](../../instructions/thinkscript-authoring.instructions.md)
