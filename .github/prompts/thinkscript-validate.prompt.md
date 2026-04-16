# ThinkScript Validation Prompt (No Code Generation)

You are validating a ThinkScript snippet for correctness and constraints.

## Inputs
- Script:
{{SCRIPT}}
- Constraints:
{{CONSTRAINTS}}

## Rules
1. **Do not generate replacement code.**
2. Return only findings and minimal fix guidance.
3. Prioritize compile blockers, then logic defects, then style issues.
4. If uncertain, mark as `needs verification`.

## Output format

### Validation Result
- Status: `pass` | `fail` | `needs verification`

### Findings
For each finding:
- Severity: `error` | `warning` | `info`
- Line/Area: `<line number or block>`
- Issue: `<what is wrong>`
- Why it matters: `<impact>`
- Minimal fix guidance: `<brief instruction, no code block>`

### Constraint Check
- Constraint: `<name>`
- Result: `pass` | `fail` | `needs verification`
- Notes: `<short note>`

### Summary
- Compile blockers: `<count>`
- Logic risks: `<count>`
- Style issues: `<count>`