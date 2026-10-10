# Production Result List

A command-line Python program for recording simulated production inspection results. It preserves the order of valid entries, counts PASS, FAIL, and REWORK outcomes, and calculates the PASS percentage.

## Features

- Accepts results until the user enters `done`, regardless of letter case or surrounding spaces.
- Stores valid results in uppercase in a list, preserving duplicates and input order.
- Rejects empty and unsupported entries without adding them to the list.
- Displays numbered entries, category counts, and a pass rate.
- Handles an empty collection without dividing by zero.

This is an educational simulation. Each entry represents a different inspected item; REWORK is an initial result, not an update to an earlier record.

## Requirements and usage

Python 3.6 or later. No additional packages are required.

From this folder, run:

```text
python main.py
```

On Windows, use `py main.py` if `python` is unavailable.

## Example

```text
Enter result (PASS/FAIL/REWORK) or 'done': pass
Enter result (PASS/FAIL/REWORK) or 'done': FAIL
Enter result (PASS/FAIL/REWORK) or 'done': rework
Enter result (PASS/FAIL/REWORK) or 'done': PASS
Enter result (PASS/FAIL/REWORK) or 'done': done
Recorded result
1. PASS
2. FAIL
3. REWORK
4. PASS
Production summary
Total items: 4
PASS count: 2
FAIL count: 1
REWORK count: 1
Pass rate: 50.00%
```

An invalid input prints `Invalid result: enter PASS, FAIL, REWORK, or 'done'.` and asks again. With no valid entries, the program prints `No valid result entered.` without a numeric report.

## Pass-rate rule

**Pass rate = PASS count / total valid results × 100.**

FAIL and REWORK entries count toward the total, but not the PASS count. For example, one PASS, one FAIL, and one REWORK produce a pass rate of `33.33%`. The calculation keeps full precision and rounds only for display.

## Functions

| Function | Responsibility |
| --- | --- |
| `calculate_pass_rate(results)` | Return the unrounded percentage for a non-empty list |
| `display_report(results)` | Handle an empty list or display numbered entries and a summary |
| `main()` | Validate input, append allowed results, and request the report |

`calculate_pass_rate()` assumes a non-empty list because `display_report()` checks first. The report uses `enumerate(results, start=1)` so numbering begins at one and stays in input order.

## Verification cases

These cases passed during review. They are documented checks, not a committed automated test suite.

| Inputs, ending with `done` | Total | PASS | FAIL | REWORK | Pass rate or result |
| --- | ---: | ---: | ---: | ---: | --- |
| PASS, FAIL, REWORK, PASS | 4 | 2 | 1 | 1 | 50.00% |
| PASS | 1 | 1 | 0 | 0 | 100.00% |
| FAIL | 1 | 0 | 1 | 0 | 0.00% |
| REWORK | 1 | 0 | 0 | 1 | 0.00% |
| PASS, PASS, PASS | 3 | 3 | 0 | 0 | 100.00% |
| PASS, FAIL, REWORK | 3 | 1 | 1 | 1 | 33.33% |
| Surrounding spaces on pass, ReWoRk, and DONE | 2 | 1 | 0 | 1 | 50.00% |
| FAIL, PASS, FAIL | 3 | 1 | 2 | 0 | 33.33%; numbered order remains FAIL, PASS, FAIL |
| No valid entries | — | — | — | — | No-valid-result message |
| Empty line, spaces, 123, READY | — | — | — | — | Four errors, then no-valid-result message |
| PASS, READY, FAIL | 2 | 1 | 1 | 0 | One error; 50.00% |
| PA SS, RE WORK | — | — | — | — | Two errors; internal spaces are not removed |

A helper check confirmed that one PASS out of three results returns an unrounded value close to `33.33333333333333`. The helper does not modify the input list.

## Skills practised

Lists, `.count()`, `enumerate()`, input validation, case normalisation, function return values, preserving entry order, and percentage formatting.

## Files

- `main.py`: completed program
- `README.md`: usage, rules, and verification cases

[Data structures](../../README.md) · [Learning roadmap](../../../ROADMAP.md)
