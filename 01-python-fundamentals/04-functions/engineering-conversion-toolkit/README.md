# Engineering Conversion Toolkit

A command-line Python application that performs common temperature and distance conversions through a reusable, function-based design.

## Features

- Converts Celsius to Fahrenheit.
- Converts Fahrenheit to Celsius.
- Converts kilometres to miles.
- Converts miles to kilometres.
- Continues running until the user chooses to exit.
- Rejects unsupported menu selections.
- Handles non-numeric input without terminating unexpectedly.
- Formats conversion results to two decimal places.

## Skills demonstrated

- Function definition and invocation
- Parameters and return values
- Menu-driven program flow
- `while` loops
- Conditional statements
- Exception handling with `try` and `except`
- Numeric calculations and formatted output
- Python's `__name__ == "__main__"` entry-point pattern

## Conversion formulas

```text
Fahrenheit = (Celsius × 9 / 5) + 32
Celsius = (Fahrenheit - 32) × 5 / 9
Miles = Kilometres × 0.621371
Kilometres = Miles × 1.60934
```

## Requirements

Python 3.6 or later. No additional packages are required.

## How to run

From this directory, run:

```text
python main.py
```

## Example

```text
Engineering Conversion Toolkit
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Kilometres to miles
4. Miles to kilometres
5. Exit

Select an option: 4
Enter distance in miles: 10
10.00 mi = 16.09 km
```

The menu appears again after each completed conversion. Selecting option `5` ends the program.

## Test cases

| Menu option | Value | Expected result |
| --- | --- | --- |
| 1 | 0 | 32.00 F |
| 1 | 100 | 212.00 F |
| 2 | 32 | 0.00 C |
| 2 | 212 | 100.00 C |
| 3 | 10 | 6.21 mi |
| 4 | 10 | 16.09 km |
| 1 | -40 | -40.00 F |
| 9 | Not requested | Invalid option message; menu returns |
| 1.5 or abc | Not requested | Invalid input message; menu returns |
| Any conversion | abc | Invalid input message; menu returns |
| 5 | Not requested | Goodbye! |

## What I learned

I practiced returning values from functions, handling invalid numeric input in each menu branch, and separating reusable calculations from the interactive program. I also learned why the entry-point guard prevents the menu from starting when the module is imported.

## Project files

```text
engineering-conversion-toolkit/
├── main.py
└── README.md
```

[All fundamentals exercises](../../README.md) · [Portfolio overview](../../../README.md)
