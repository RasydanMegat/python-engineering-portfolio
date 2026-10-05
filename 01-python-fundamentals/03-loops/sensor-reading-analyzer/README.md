# Sensor Reading Analyzer

A command-line Python program that classifies equipment-temperature readings and produces an operational summary.

## Purpose

This exercise combines loops, conditional classification, counters, accumulators, validation, and summary statistics in an engineering-style sensor-monitoring scenario.

## Features

- Accepts any quantity of temperature readings
- Stops when `done` is entered in any letter case
- Classifies readings as low, normal, or high
- Counts each temperature classification
- Calculates average, minimum, and maximum temperatures
- Continues after invalid input
- Handles an empty dataset safely
- Formats temperature statistics to two decimal places

## Temperature classifications

| Temperature | Classification |
|---:|---|
| Below 20 C | Low |
| 20 C through 70 C | Normal |
| Above 70 C | High |

## Skills demonstrated

- `while` loops
- Sentinel-controlled iteration
- `break` and `continue`
- Conditional classification
- Multiple counters
- Accumulators and averages
- Minimum and maximum tracking
- Repeated exception handling
- Boundary-value testing
- Formatted engineering output

## Requirements

Python 3.6 or later. No additional packages are required.

## How to run

From this directory, run:

```text
python main.py
```

## Example

```text
Enter sensor temperature or 'done': 15
Enter sensor temperature or 'done': 25
Enter sensor temperature or 'done': 40
Enter sensor temperature or 'done': 70
Enter sensor temperature or 'done': 75
Enter sensor temperature or 'done': done

Sensor Reading Summary
Total readings: 5
Low readings: 1
Normal readings: 3
High readings: 1
Average temperature: 45.00 C
Minimum temperature: 15.00 C
Maximum temperature: 75.00 C
```

## Test cases

| Scenario | Values |
|---|---|
| Mixed classifications | 15, 25, 40, 70, 75 |
| Exact boundaries | 19.9, 20, 70, 70.1 |
| Invalid entries | cold, 30, error, 80 |
| Negative reading | -5 |
| No readings | done |
| Case-insensitive sentinel | 35, DONE |

## What I learned

I learned how to combine loop control with conditional classification, maintain independent category counters, calculate statistics after data collection, and safely handle invalid or empty input.

## Project files

- [main.py](main.py) — completed implementation
- [README.md](README.md) — usage, examples and manual checks

[All fundamentals exercises](../../README.md) · [Portfolio overview](../../../README.md)
