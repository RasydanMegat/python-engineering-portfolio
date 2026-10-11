# Sorted Equipment Results

A command-line Python program that collects simulated equipment test scores and ranks them from highest to lowest. Equal scores are ordered alphabetically by equipment name.

## Features

- Stores one integer score from 0 through 100 for each equipment name.
- Normalizes names to uppercase and removes surrounding spaces while preserving internal spaces.
- Rejects duplicate names without overwriting the original score.
- Rejects empty names, non-integer scores, and scores outside the accepted range.
- Produces a numbered ranking without modifying the original dictionary.
- Handles an empty collection with a clear message.

These scores are invented for programming practice; they do not represent real equipment measurements or safety decisions.

## Requirements and usage

Python 3.7 or later. No additional packages are needed. From this folder, run:

```text
python main.py
```

On Windows, use `py main.py` if `python` is unavailable.

## Example

```text
Equipment name or 'done': pump
Score (0-100): 88
Equipment name or 'done': FAN
Score (0-100): 92
Equipment name or 'done': Motor
Score (0-100): 88
Equipment name or 'done': done
Equipment results
Total equipment: 3
Rankings:
1. FAN - 92
2. MOTOR - 88
3. PUMP - 88
```

Entering `done` without any valid results prints `No equipment results entered.` An invalid score returns to the equipment-name prompt without storing that entry. A duplicate name is rejected before asking for another score.

## How sorting works

The dictionary maps each name to its score. `results.items()` supplies `(name, score)` tuples. The sorting key `(-item[1], item[0])` compares the negative score first, then the name. This puts higher original scores first and resolves equal scores alphabetically.

`sorted()` returns a new list containing the original pairs; the scores stay positive or zero and the dictionary is unchanged. `enumerate(ranked, start=1)` numbers the report rows.

## Functions

| Function | Responsibility |
| --- | --- |
| `sort_results(results)` | Return a list of pairs sorted by score descending, then name ascending |
| `display_report(results)` | Print the empty-results message or the numbered ranking |
| `main()` | Collect names and scores, validate entries, and request one report |

## Verification cases

These cases passed during review. They are documented checks, not a committed automated test suite.

| Scenario | Expected result |
| --- | --- |
| Enter done immediately | No-results message; no numeric report |
| PUMP 88 | One result: PUMP - 88 |
| PUMP 88, FAN 92, MOTOR 88 | FAN, MOTOR, PUMP ranking |
| PUMP 100, FAN 0 | Both boundary scores accepted; PUMP first |
| FAN 70, PUMP 90, LED 80 | PUMP, LED, FAN ranking |
| Enter PUMP 80, then the same name with different case and spaces | Duplicate rejected; original score retained; no second score prompt |
| Empty and spaces-only names | Invalid-name messages; no entries stored |
| A text score followed by a valid entry | Invalid score rejected; valid entry retained |
| Scores -1, 101, and 2.5 | All rejected without storing results |
| Name with surrounding and internal spaces; score with surrounding spaces | Surrounding spaces removed; internal name spaces preserved |
| MOTOR 88, PUMP 88, FAN 88 | FAN, MOTOR, PUMP alphabetical tie order |

Helper checks confirmed that sorting returns a list of tuples, leaves the dictionary unchanged, produces no printed output, and returns an empty list for an empty dictionary.

## Skills practised

Dictionaries, tuples, `sorted()`, sorting keys, lambda expressions, `enumerate()`, duplicate detection, and input validation.

## Files

- `main.py`: completed program
- `README.md`: usage, sorting rules, and verification cases

[Data structures](../../README.md) · [Learning roadmap](../../../ROADMAP.md)
