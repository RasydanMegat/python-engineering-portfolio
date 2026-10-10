# Sensor Statistics

A command-line Python program that stores simulated temperature readings in a list and displays their count, minimum, maximum, and average.

## Features

- Collects readings until the user enters `done`, ignoring letter case and surrounding whitespace.
- Stores valid readings as floats, including negatives, zero and duplicates.
- Rejects non-numeric input, NaN, and positive or negative infinity.
- Handles an empty collection without attempting invalid calculations.
- Preserves numeric precision during calculation and formats summary temperatures to two decimal places.

These are keyboard-entered educational readings; the program does not connect to physical sensors. Extreme floating-point overflow is outside the exercise scope.

## Requirements and usage

Python 3.6 or later. No additional packages are required.

From this folder:

```text
python main.py
```

On Windows, use `py main.py` if `python` is unavailable.

## Examples

```text
Enter temperature in C or 'done': 10
Enter temperature in C or 'done': 20
Enter temperature in C or 'done': 30
Enter temperature in C or 'done': done
Temperature summary
Reading count: 3
Lowest temperature: 10.00 C
Highest temperature: 30.00 C
Average temperature: 20.00 C
```

```text
Enter temperature in C or 'done': hello
Invalid input: enter a number or 'done'.
Enter temperature in C or 'done': nan
Invalid temperature: enter a finite number.
Enter temperature in C or 'done': -5
Enter temperature in C or 'done': 5
Enter temperature in C or 'done': DONE
Temperature summary
Reading count: 2
Lowest temperature: -5.00 C
Highest temperature: 5.00 C
Average temperature: 0.00 C
```

Entering `done` before any valid reading prints `No valid readings entered.`

## Functions

| Function | Responsibility |
| --- | --- |
| `calculate_average(readings)` | Return the unrounded average of a non-empty list |
| `display_summary(readings)` | Handle an empty collection or print the statistics |
| `main()` | Collect, validate and append readings, then request the summary |

The average helper assumes a non-empty list; the summary function checks this before calling it. Neither helper changes the input list. `math.isfinite()` rejects non-finite numbers after numeric conversion succeeds.

## Verification cases

These input/output cases passed during review. They are documented checks, not a committed automated test suite.

| Inputs, ending with `done` | Count | Lowest | Highest | Average or result |
| --- | --- | --- | --- | --- |
| 10, 20, 30 | 3 | 10.00 | 30.00 | 20.00 |
| 25.5 | 1 | 25.50 | 25.50 | 25.50 |
| -5, 0, 5 | 3 | -5.00 | 5.00 | 0.00 |
| 7, 7, 7 | 3 | 7.00 | 7.00 | 7.00 |
| 30, 10, 20 | 3 | 10.00 | 30.00 | 20.00 |
| 1, 2, 2 | 3 | 1.00 | 2.00 | 1.67 |
| Surrounding spaces on 2.5, 7.5 and uppercase DONE | 2 | 2.50 | 7.50 | 5.00 |
| No readings | — | — | — | No valid readings message |
| Text, empty input, whitespace only | — | — | — | Three input errors, then no valid readings message |
| nan, inf, -inf | — | — | — | Three finite-number errors, then no valid readings message |
| 10, hello, nan, 20 | 2 | 10.00 | 20.00 | Two errors; average 15.00 |

Additional checks verified that the average of `[1.0, 2.0, 2.0]` retains its precision and that neither helper mutates the list.

## Skills practised

Lists, `.append()`, `len()`, `sum()`, `min()`, `max()`, finite-number validation, exception handling, functions, and formatted output.

## Files

- `main.py`: completed program
- `README.md`: usage, behaviour, and verification cases

[Data structures](../../README.md) · [Learning roadmap](../../../ROADMAP.md)
