# Most Common Error

A command-line Python program that counts simulated error codes, ranks them by frequency, and reports every code tied for the highest count.

## Features

- Accepts E01, E02, and E03 until the user enters `done`.
- Normalizes letter case and surrounding spaces.
- Rejects unsupported codes without changing the counts.
- Sorts by frequency descending, with alphabetical ordering for ties.
- Identifies all most common codes, including when every code ties.
- Handles an empty collection without calling `max()` on empty data.

These codes are invented for programming practice. The program does not connect to real equipment.

## Requirements and usage

Python 3.7 or later. No additional packages are needed. From this folder, run:

```text
python main.py
```

On Windows, use `py main.py` if `python` is unavailable.

## Example

```text
Enter error code (E01/E02/E03) or 'done': E03
Enter error code (E01/E02/E03) or 'done': E01
Enter error code (E01/E02/E03) or 'done': E03
Enter error code (E01/E02/E03) or 'done': E02
Enter error code (E01/E02/E03) or 'done': E01
Enter error code (E01/E02/E03) or 'done': done
Error frequency ranking
Total reports: 5
Unique codes: 3
Rankings:
1. E01 - 2
2. E03 - 2
3. E02 - 1
Most common codes: E01, E03
Highest frequency: 2
```

Invalid input prints `Invalid code: enter E01, E02, E03, or 'done'.` and prompts again. If no valid code was entered, the program prints `No valid error codes entered.` without a numeric report.

## How it works

A dictionary stores each observed code and its frequency. `.get(code, 0)` lets a new code start at zero before incrementing it. Ranking uses a sorting key containing the negative frequency and the code name.

The most-common-code helper finds the maximum frequency, collects every code with that frequency, and returns an alphabetically sorted list. `", ".join(common_codes)` formats that list for the report. The report distinguishes total entries (`sum(counts.values())`) from distinct codes (`len(counts)`).

## Functions

| Function | Responsibility |
| --- | --- |
| `record_error(counts, code)` | Increase a validated code's frequency in the existing dictionary |
| `rank_errors(counts)` | Return ranked code/frequency tuples without modifying the dictionary |
| `find_most_common(counts)` | Return all highest-frequency code names alphabetically, or an empty list |
| `display_report(counts)` | Print the empty message or ranked summary |
| `main()` | Validate input, record codes, and request one report |

## Verification cases

These cases passed during review. They are documented checks, not a committed automated test suite.

| Codes entered before done | Expected result |
| --- | --- |
| None | No-valid-codes message; no numeric report |
| E02 | Total 1; unique 1; E02 is most common at frequency 1 |
| E03, E03, E03 | Total 3; unique 1; E03 is most common at frequency 3 |
| E03, E01, E03, E02, E01 | Total 5; ranking E01, E03, E02; leaders E01 and E03 at frequency 2 |
| E03, E02, E01 | Alphabetical ranking; all three are leaders at frequency 1 |
| E01, E02, E02 | E02 ranks first despite being entered later |
| E03, E03, E03, E02, E01 | E03 first; E01 before E02 for the lower-frequency tie |
| Mixed case and surrounding spaces | Normalized codes and done command accepted |
| Empty input, spaces, E04, abc | Four invalid-code messages; no counts stored |
| E01, E04, E01 | Invalid code rejected; total 2; E01 count 2 |
| E 01, 01 | Both rejected |

Helper checks confirmed that recording updates the original dictionary, ranking and leader selection leave it unchanged and do not print, and both query helpers return an empty list for empty input.

## Skills practised

Dictionary frequency counting, sorting keys, tuples, maximum values, tied results, list construction, string joining, and input validation.

## Files

- `main.py`: completed program
- `README.md`: usage, behavior, and verification cases

[Data structures](../../README.md) · [Learning roadmap](../../../ROADMAP.md)
