# Equipment Temperature Monitor

A command-line Python program that classifies an equipment temperature and displays its operating status.

## Purpose

This exercise applies conditional logic to a simple equipment-monitoring scenario.

## Features

- Accepts whole-number and decimal temperatures
- Classifies four operating-temperature ranges
- Distinguishes normal, warning, and critical conditions
- Handles boundary values correctly
- Handles non-numeric input without crashing

## Temperature ranges

| Temperature | Status |
|---:|---|
| Below 20 C | WARNING: Temperature too low |
| 20 C through 70 C | Equipment temperature normal |
| Above 70 C through 80 C | WARNING: Equipment temperature high |
| Above 80 C | CRITICAL: Equipment overheating |

## Skills demonstrated

- Numeric user input
- Floating-point conversion
- `if`, `elif`, and `else`
- Comparison operators
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

Normal operation:

```text
Enter equipment temperature (C): 55
Equipment temperature normal
```

Critical condition:

```text
Enter equipment temperature (C): 95
CRITICAL: Equipment overheating
```

Invalid input:

```text
Enter equipment temperature (C): hot
Invalid input: enter a numeric temperature
```

## Test cases

| Input | Expected result |
|---:|---|
| 19 | WARNING: Temperature too low |
| 20 | Equipment temperature normal |
| 55.5 | Equipment temperature normal |
| 70 | Equipment temperature normal |
| 70.1 | WARNING: Equipment temperature high |
| 80 | WARNING: Equipment temperature high |
| 80.1 | CRITICAL: Equipment overheating |
| -5 | WARNING: Temperature too low |
| hot | Invalid input message |

## What I learned

I learned how Python evaluates conditional branches from top to bottom, how to define non-overlapping numeric ranges, and why testing exact boundary values is essential.

## Project files

- [main.py](main.py) — completed implementation
- [README.md](README.md) — usage, examples and manual checks

[All fundamentals exercises](../../README.md) · [Portfolio overview](../../../README.md)
