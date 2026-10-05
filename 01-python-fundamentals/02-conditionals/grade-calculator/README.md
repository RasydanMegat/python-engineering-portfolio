# Grade Calculator

A command-line Python program that validates a numeric score and converts it into a letter grade.

## Purpose

This exercise applies ordered conditional logic and range validation to a grading scenario.

## Features

- Accepts whole-number and decimal scores
- Validates the allowed range from 0.0 to 1.0
- Converts valid scores into grades A through F
- Handles every exact grade boundary
- Handles non-numeric input without crashing

## Grade ranges

| Score | Grade |
|---:|:---:|
| 0.9 through 1.0 | A |
| 0.8 through below 0.9 | B |
| 0.7 through below 0.8 | C |
| 0.6 through below 0.7 | D |
| Below 0.6 | F |

## Skills demonstrated

- Numeric user input
- Floating-point conversion
- Range validation
- `if`, `elif`, and `else`
- Comparison and Boolean operators
- Ordered decision logic
- Boundary-value testing
- Exception handling with `try` and `except`

## Requirements

Python 3.6 or later. No additional packages are required.

## How to run

From this directory, run:

```text
python main.py
```

## Example

Valid score:

```text
Enter score (0.0-1.0): 0.86
Grade: B
```

Out-of-range score:

```text
Enter score (0.0-1.0): 1.2
Invalid score: enter a value from 0.0 to 1.0
```

Invalid input:

```text
Enter score (0.0-1.0): excellent
Invalid input: enter a numeric score
```

## Test cases

| Input | Expected result |
|---:|---|
| 1.0 | Grade: A |
| 0.9 | Grade: A |
| 0.89 | Grade: B |
| 0.8 | Grade: B |
| 0.79 | Grade: C |
| 0.7 | Grade: C |
| 0.69 | Grade: D |
| 0.6 | Grade: D |
| 0.59 | Grade: F |
| 0.0 | Grade: F |
| 1.01 | Invalid score message |
| -0.01 | Invalid score message |
| abc | Invalid input message |

## What I learned

I learned how to validate a numeric range before processing data, arrange conditions from the highest boundary downward, and test exact boundaries to prevent classification errors.

## Project files

- [main.py](main.py) — completed implementation
- [README.md](README.md) — usage, examples and manual checks

[All fundamentals exercises](../../README.md) · [Portfolio overview](../../../README.md)
