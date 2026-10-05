# Number Analyzer

A command-line Python program that accepts an unknown quantity of numbers and displays a statistical summary when the user enters `done`.

## Purpose

This exercise applies loops, sentinel values, accumulators, counters, repeated validation, and largest/smallest tracking to a numeric data-analysis task.

## Features

- Accepts any quantity of whole or decimal numbers
- Stops when `done` is entered in any letter case
- Ignores invalid entries after displaying a clear message
- Calculates count, total, average, largest, and smallest values
- Supports positive and negative numbers
- Handles an empty dataset without dividing by zero
- Formats summary values to two decimal places

## Skills demonstrated

- `while` loops
- Sentinel-controlled iteration
- `break` and `continue`
- Counters and accumulators
- Largest and smallest value tracking
- `None` as an initial state
- Repeated exception handling
- Numeric summary calculations
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
Enter a number or 'done': 10
Enter a number or 'done': 20
Enter a number or 'done': abc
Invalid input: enter a number or 'done'
Enter a number or 'done': 5
Enter a number or 'done': 15
Enter a number or 'done': done

Number Summary
Count: 4
Total: 50.00
Average: 12.50
Largest: 20.00
Smallest: 5.00
```

## Test cases

| Scenario | Values |
|---|---|
| Positive numbers | 10, 20, 5, 15 |
| Mixed numbers | -5, 10, -2.5, 7.5 |
| Single number | 4.25 |
| Invalid then valid | hello, 8, bad, 12 |
| No numbers | done |
| Case-insensitive sentinel | 3, DONE |

## What I learned

I learned how to control an indefinite loop with a sentinel value, skip invalid entries without ending the program, maintain running statistics, and safely handle an empty dataset.

## Project files

- [main.py](main.py) — completed implementation
- [README.md](README.md) — usage, examples and manual checks

[All fundamentals exercises](../../README.md) · [Portfolio overview](../../../README.md)
