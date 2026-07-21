# IBTC Python 2026 — Course Workspace

This repo holds daily coding exercises for the IBT Python bootcamp (2026 cohort). Each `dayNN*` folder is a self-contained lesson; there is no shared package structure, build system, or dependency manifest — every file runs standalone with `python <file>.py`.

## Layout

- `day01and01/` — fundamentals: variables, control flow, a tip calculator (`class_work.py`, `practice.py`, `tip_calculator.py`), with a `README.md` per lesson.
- `day02/` — continuation of fundamentals, same file pattern as day01.
- `day03/` — `main.py`.
- `day04/` — intro to OOP: `Account` class with encapsulated balance (`account.py`), plus `Practice.py`.
- `day05/` — OOP continued: `Account`, `SavingsAccount`, `CurrentAccount` with polymorphism (`accounts.py`).
- `practicewithGroup/` — group exercises (`main.py`).

## Conventions observed in this repo

- Type hints on method signatures and return types (see `day05/accounts.py`).
- Private state via name-mangled attributes (`self.__balance`) exposed through `@property`.
- Input validation via `raise ValueError(...)` with a clear message, not silent clamping.
- f-strings for formatted output/statements.
- Each day's `if __name__ == "__main__":` block is used as a runnable demo/smoke test — there is no separate test suite or test runner.

## Working in this repo

- No virtualenv, requirements.txt, or package manager is set up — assume stdlib-only unless a day's folder says otherwise.
- Keep new work inside the relevant `dayNN` folder rather than introducing shared modules across days, matching the existing per-lesson isolation.
- When writing or reviewing Python here, use the `python-expert` skill.
