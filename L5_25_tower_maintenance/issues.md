# Lab 5: Static Code Analysis

## Issue Documentation

| Issue | Type | Original Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Hardcoded password | Security | 6 | Password was stored directly in source code. | Removed the unused hardcoded credential. |
| SQL query construction | Security | 11 | INSERT query used string formatting to construct SQL. | Used parameterized SQL with placeholders. |
| Unsafe pickle deserialization | Security | 1, 43 | Pickle was used to serialize and deserialize database records unnecessarily. | Removed pickle and returned database records directly. |
| Missing module docstring | Code quality | 1 | Module did not explain its purpose. | Added a module docstring. |
| Missing function docstrings | Code quality | Multiple | Functions lacked documentation. | Added descriptive function docstrings. |
| Invalid function naming | Code quality | 10, 15, 34 | Function names used camelCase instead of snake_case. | Renamed functions using snake_case. |
| Global statement | Code quality | 16 | A global counter was modified inside a function. | Made the counter local to main(). |
| Broad exception handling | Code quality | 20 | A general Exception handler could hide unexpected errors. | Removed unnecessary broad exception handling. |
| Unnecessary else | Code quality | 38 | An else followed a return statement. | Removed the unnecessary else. |
| Long lines | Formatting | 5, 11, 18, 35, 43 | Several lines exceeded the configured length limit. | Split long statements across multiple lines. |
| Excess blank lines | Formatting | 25 | Too many blank lines were present. | Removed excess blank lines. |
| Missing operator whitespace | Formatting | 50 | An operator did not follow PEP 8 spacing conventions. | Corrected whitespace. |

## Verification

- Pylint score: 10.00/10
- Bandit: No issues identified
- Flake8: No violations displayed

