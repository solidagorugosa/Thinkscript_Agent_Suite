---
description: "Generate a complete thinkScript study or strategy from requirements, using documented syntax and constraints."
name: "ThinkScript Generate"
argument-hint: "What should the script do? Include inputs, timeframe, and whether this is a study or strategy."
agent: "agent"
---
Create a production-ready thinkScript script from the user's requirements.

Requirements for your output:
- Return one complete script block.
- Use idiomatic thinkScript (`input`, `def`, `plot`, and `AddOrder` when strategy is requested).
- Respect documented constraints (aggregation and price type limits, semicolons, valid conditional forms).
- Keep comments concise and only where they add clarity.

Before finalizing, do a quick self-check for:
- Missing semicolons
- Invalid function/constant usage
- Incompatible argument combinations
