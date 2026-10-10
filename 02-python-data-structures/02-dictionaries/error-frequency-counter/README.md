# Error Frequency Counter

A command-line Python program that counts simulated error codes with a dictionary and reports their frequencies in the order each code first appeared.

## Features

- Accepts `E01`, `E02`, and `E03` until the user enters `done`.
- Ignores surrounding spaces and letter case when reading input.
- Rejects invalid codes without changing the counts.
- Reports the total number of valid entries, number of unique codes, and frequency of each code.
- Handles a session with no valid codes without printing a numeric report.

The error codes are invented for programming practice; they do not represent real equipment faults.

## Run

Requires Python 3.7 or later. No additional packages are needed. From this folder, run:

```text
python main.py
```

On Windows, use `py main.py` if `python` is unavailable.

## Example

```text
Enter error code (E01/E02/E03) or 'done': e02
Enter error code (E01/E02/E03) or 'done': E01
Enter error code (E01/E02/E03) or 'done': E02
Enter error code (E01/E02/E03) or 'done': done
Error frequency report
Total reports: 3
Unique codes: 2
Counts:
E02: 2
E01: 1
```

Invalid input prints `Invalid code: enter E01, E02, E03, or 'done'.` and prompts again. Entering `done` without any valid codes prints `No valid error codes entered.`

## How it works

`record_error(counts, code)` updates the existing dictionary. `counts.get(code, 0)` reads the current count, using zero for a code not yet recorded. `display_report(counts)` uses `sum(counts.values())` for the total, `len(counts)` for the unique count, and `counts.items()` to print each code and frequency. Python dictionaries preserve first-insertion order, so repeated codes do not move in the report.

## Verification

These input/output cases passed during review. They are documented checks, not a committed automated test suite.

| Inputs, ending with `done` | Expected result |
| --- | --- |
| E02, E01, E02 | Total 3; unique 2; E02: 2 before E01: 1 |
| E01 | Total 1; unique 1; E01: 1 |
| E01, E01, E01 | Total 3; unique 1; E01: 3 |
| E03, E02, E01 | Total 3; unique 3; first-seen order retained |
| E02, E01, E02, E03 | Total 4; unique 3; E02, E01, E03 order |
| Surrounding spaces and lowercase codes | Valid codes normalized to uppercase |
| No codes | No-valid-codes message; no numeric report |
| Empty line, spaces, E04 | Three errors, then no-valid-codes message |
| E01, E04, E01 | One error; total 2; E01: 2 |
| E 01, 01 | Two errors; no-valid-codes message |

## Files

- `main.py`: completed program
- `README.md`: usage and verification cases

[Data structures](../../README.md) · [Learning roadmap](../../../ROADMAP.md)
