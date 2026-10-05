# Employee Pay Calculator

A command-line Python program that calculates an employee's total pay from the number of hours worked and the hourly pay rate.

## Purpose

This exercise applies introductory Python concepts to a small payroll calculation.

## Features

- Accepts decimal hours and hourly rates
- Calculates total pay using `hours x rate`
- Displays the result with two decimal places
- Detects negative hours and negative rates separately
- Handles non-numeric input without crashing

## Skills demonstrated

- User input
- Variables and floating-point values
- Arithmetic
- Conditional statements
- Boolean operators
- Exception handling with `try` and `except`
- Formatted output using f-strings

## Requirements

Python 3.6 or later. No additional packages are required.

## How to run

From this directory, run:

```text
python main.py
```

## Example

```text
Enter hours worked: 35
Enter hourly rate: 12.50
Hours Worked: 35.0
Hourly Rate: 12.5
Total Pay: $437.50
```

## Validation examples

Negative hours:

```text
Enter hours worked: -5
Enter hourly rate: 12
Hours cannot be negative
```

Invalid input:

```text
Enter hours worked: abc
Invalid input: enter numeric values
```

## Test cases

| Hours | Rate | Expected result |
|---:|---:|---|
| 35 | 12.50 | Total Pay: $437.50 |
| 8 | 15 | Total Pay: $120.00 |
| 0 | 20 | Total Pay: $0.00 |
| 10.5 | 11.25 | Total Pay: $118.12 |
| -5 | 12 | Hours cannot be negative |
| 10 | -12 | Rate cannot be negative |
| -5 | -12 | Hours and rate cannot be negative |
| abc | 12 | Invalid input message |

## What I learned

I learned how to collect and convert user input, validate multiple conditions, calculate a result, handle invalid input with `try` and `except`, and format monetary output to two decimal places.

## Project files

- [main.py](main.py) — completed implementation
- [README.md](README.md) — usage, examples and manual checks

[All fundamentals exercises](../../README.md) · [Portfolio overview](../../../README.md)
