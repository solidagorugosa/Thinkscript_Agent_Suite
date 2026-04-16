# Strategy Conversion Prompt (Plain English to ThinkScript)

Convert the user’s plain-English strategy into ThinkScript strategy code.

## Inputs
- Strategy rules:
{{RULES}}
- Symbol/timeframe assumptions:
{{ASSUMPTIONS}}
- Risk/exit rules:
{{RISK_RULES}}

## Requirements
1. Produce valid ThinkScript strategy code.
2. Use clear inputs for tunable parameters.
3. Include entry and exit conditions explicitly.
4. Avoid unsupported constructs.
5. Add short comments for each logic section.

## Output format

### Assumptions
- `<bulleted assumptions inferred from user rules>`

### ThinkScript Strategy
```thinkscript
<strategy code>
```

### Mapping (Rule → Code)
- Rule: `<plain-English rule>`
- Implementation: `<code section reference>`

### Validation Checklist
- [ ] Entries implemented
- [ ] Exits implemented
- [ ] Risk controls represented
- [ ] Parameters externalized as inputs