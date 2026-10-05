# Engineering Unit Converter

A command-line Python program that converts three common engineering measurements from metric units to imperial units.

## Purpose

This exercise applies introductory Python arithmetic and input handling to temperature, length, and mass conversions.

## Features

- Converts Celsius to Fahrenheit
- Converts millimetres to inches
- Converts kilograms to pounds
- Supports whole numbers, decimals, zero, and negative temperatures
- Handles non-numeric input without crashing
- Formats results to appropriate decimal precision

## Formulas

```text
fahrenheit = (celsius x 9 / 5) + 32
inches = millimetres / 25.4
pounds = kilograms x 2.20462
```

## Skills demonstrated

- User input
- Variables and floating-point values
- Arithmetic expressions
- Operator precedence
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
Enter temperature in Celsius: 25
Enter length in millimetres: 100
Enter mass in kilograms: 10

Conversion Results
Temperature: 25.00 C = 77.00 F
Length: 100.00 mm = 3.937 in
Mass: 10.00 kg = 22.05 lb
```

## Test cases

| Celsius | Millimetres | Kilograms | Expected conversions |
|---:|---:|---:|---|
| 25 | 100 | 10 | 77.00 F, 3.937 in, 22.05 lb |
| 0 | 0 | 0 | 32.00 F, 0.000 in, 0.00 lb |
| 37.5 | 12.7 | 2.5 | 99.50 F, 0.500 in, 5.51 lb |
| -40 | 25.4 | 1 | -40.00 F, 1.000 in, 2.20 lb |
| abc | 100 | 10 | Invalid input message |

Invalid input was also tested at the length and mass prompts.

## What I learned

I learned how to translate engineering formulas into Python expressions, collect and convert multiple numeric inputs, control decimal precision with f-strings, and handle invalid input using `try` and `except`.

## Project files

- [main.py](main.py) — completed implementation
- [README.md](README.md) — usage, examples and manual checks

[All fundamentals exercises](../../README.md) · [Portfolio overview](../../../README.md)
