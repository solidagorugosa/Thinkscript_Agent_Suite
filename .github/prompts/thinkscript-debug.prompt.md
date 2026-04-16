---
description: "Debug thinkScript code by finding syntax and logic errors, then return corrected code and root-cause notes."
name: "ThinkScript Debug"
argument-hint: "Paste thinkScript code and symptoms/errors."
agent: "agent"
---
Debug the provided thinkScript code.

Process:
1. Identify compile-time syntax/type errors first.
2. Identify likely runtime/behavior issues second.
3. Return corrected code.
4. Provide a short root-cause list mapping each fix to the issue.

Constraints:
- Preserve original intent unless the user asks for behavior changes.
- Prefer smallest valid edits.
- Use documented thinkScript forms when there are multiple options.
