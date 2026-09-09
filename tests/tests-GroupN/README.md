## Group N Capstone Development

This fork contains exploratory development and testing completed by Group N
for the CS4273 capstone project.

Our project is investigating the development of a user-friendly interface for
Zero2Neuro. Current work explores the proposed system at several levels:

- **Backend:** Flask and FastAPI
- **Frontend:** React with TypeScript
- **Configuration and Validation:** Pydantic and JSON Schema
- **Existing Zero2Neuro Testing:** Unit tests of selected core modules

### Current Testing Work

Unit tests have been developed for selected components of the existing
Zero2Neuro codebase to better understand current behavior and identify
testable functionality.

Current test coverage includes:

- `plugin_base.py`
- `plugin_manager.py`
- `parser.py`
- `zero2neuro_debug.py`

Testing work is currently maintained on the `unit-tests-y` branch.

### Related Interface Prototype

A separate prototype repository was created to explore interface-specific
functionality without modifying the existing Zero2Neuro core repository.

The prototype includes a focused configuration-validation feature explored across Python, JavaScript, and Java.

Repository:
[Zero2Neuro Interface Prototype](https://github.com/Alex-E-Mitchell/zero2neuro-interface.git)

This language-level comparison complements the broader technology evaluation being conducted for the proposed interface.

### Development Status

This work is exploratory and represents ongoing evaluation rather than a
final technology or architecture selection. Additional implementations,
tests, and documentation may be added as the project develops.