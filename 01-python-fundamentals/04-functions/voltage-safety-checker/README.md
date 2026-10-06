# Voltage Safety Checker

A command-line Python program that validates simulated voltage readings and classifies them as low, normal, or high according to defined exercise ranges.

The limits are invented rules for this software exercise. They are not electrical safety limits for real equipment.

## Features

- Accepts repeated voltage readings until the user enters `done`.
- Rejects negative, `nan`, and infinite values.
- Classifies readings using exact boundary conditions.
- Continues running after invalid input.
- Displays readings to two decimal places while preserving the original value for classification.

## Skills demonstrated

- Function parameters and return values
- Boolean validation functions
- `math.isfinite()` for non-finite numeric input
- Conditional ranges and boundary testing
- `while` loops and sentinel input
- Exception handling with `try` and `except`
- Separation of validation, classification, and user interaction
- Python's `__name__ == "__main__"` entry-point pattern

## Voltage ranges

| Voltage | Status |
| ---: | --- |
| `0 <= voltage < 3.0` | `LOW` |
| `3.0 <= voltage <= 3.6` | `NORMAL` |
| `voltage > 3.6` | `HIGH` |

## Requirements

Python 3.6 or later. No additional packages are required.

## Run the program

From this directory, run:

```text
python main.py
```

On Windows, use `py main.py` if `python` is unavailable.

## Example

```text
Enter voltage in V or 'done': 2.5
Voltage: 2.50 V | Status: LOW
Enter voltage in V or 'done': 3.3
Voltage: 3.30 V | Status: NORMAL
Enter voltage in V or 'done': 4.2
Voltage: 4.20 V | Status: HIGH
Enter voltage in V or 'done': nan
Invalid voltage: enter a finite value of 0 V or above.
Enter voltage in V or 'done': done
Goodbye!
```

## Test cases

| Input | Expected result |
| --- | --- |
| `0` | `Voltage: 0.00 V \| Status: LOW` |
| `2.99` | `Voltage: 2.99 V \| Status: LOW` |
| `3.0` | `Voltage: 3.00 V \| Status: NORMAL` |
| `3.6` | `Voltage: 3.60 V \| Status: NORMAL` |
| `3.61` | `Voltage: 3.61 V \| Status: HIGH` |
| `3.601` | Displays `3.60 V`, but status is `HIGH` |
| `-0.1` | Invalid voltage message |
| `abc` or an empty line | Invalid input message |
| `nan`, `inf`, or `-inf` | Invalid voltage message |
| ` 3.3 ` | Normal reading |
| ` DONE ` | Goodbye message and exit |

## What I learned

I practised returning Boolean values from a validation function, checking finite numeric input, preserving full numeric precision for classification, and testing exact boundaries before formatting display output.

## Project files

```text
voltage-safety-checker/
├── main.py
└── README.md
```
