# Python Engineering Portfolio

Practical Python exercises documenting my progress toward software, firmware, and embedded systems engineering.

I am building a foundation in programming through small, complete command-line programs: writing an initial implementation, checking edge cases, using review feedback, and documenting the results.

**Progress: 7 completed exercises.** Current focus: functions and input validation. Next planned exercise: Voltage Safety Checker.

## Start here

| Selected work | What to look for |
| --- | --- |
| [Engineering Conversion Toolkit](01-python-fundamentals/04-functions/engineering-conversion-toolkit/) | Four reusable conversion functions, a repeating menu, and input error handling. |
| [Sensor Reading Analyzer](01-python-fundamentals/03-loops/sensor-reading-analyzer/) | Separate category counters, summary statistics, and empty-input handling. |
| [Number Analyzer](01-python-fundamentals/03-loops/number-analyzer/) | Running statistics and minimum/maximum tracking without storing every reading. |

These are learning exercises using keyboard input. The engineering examples simulate measurements; they do not connect to physical devices.

## Completed exercise index

| Exercise | Skills demonstrated |
| --- | --- |
| [Employee Pay Calculator](01-python-fundamentals/01-variables-and-input/employee-pay-calculator/) | Input validation and arithmetic |
| [Engineering Unit Converter](01-python-fundamentals/01-variables-and-input/engineering-unit-converter/) | Formulas and formatted output |
| [Equipment Temperature Monitor](01-python-fundamentals/02-conditionals/equipment-temperature-monitor/) | Conditional ranges and boundary checks |
| [Grade Calculator](01-python-fundamentals/02-conditionals/grade-calculator/) | Range validation and ordered conditions |
| [Number Analyzer](01-python-fundamentals/03-loops/number-analyzer/) | Loops, running totals, minimum and maximum |
| [Sensor Reading Analyzer](01-python-fundamentals/03-loops/sensor-reading-analyzer/) | Classification, counters and summary statistics |
| [Engineering Conversion Toolkit](01-python-fundamentals/04-functions/engineering-conversion-toolkit/) | Reusable functions and menu input handling |

## Skills demonstrated

- **Python fundamentals:** numeric input, arithmetic, strings, conditions and loops.
- **Problem solving:** classification, boundary checks, running statistics and empty-data handling.
- **Program structure:** functions, parameters, return values and a program entry point.
- **Development practice:** manual test cases, clear documentation, review and Git version control.

Firmware and embedded systems are career interests. Object-oriented programming is a planned learning stage; hardware integration, C/C++, and device communication are future learning areas.

## Run an exercise

Requires Python 3.6 or later. The current exercises use Python's built-in features and need no additional packages.

Clone this repository, then run an exercise from the repository root:

```text
git clone https://github.com/rsydnmgt2311/python-engineering-portfolio.git
cd python-engineering-portfolio
python 01-python-fundamentals/04-functions/engineering-conversion-toolkit/main.py
```

On Windows, use `py` if `python` is unavailable. Each exercise README includes sample input, output, and manual test cases.

## Learning path

| Stage | Status | Explore |
| --- | --- | --- |
| Python fundamentals | 7 of 10 exercises complete | [Fundamentals](01-python-fundamentals/) |
| Data structures | Planned | [Lists, dictionaries and sorting](02-python-data-structures/) |
| Object-oriented programming | Planned | [Classes, objects and OOP projects](06-object-oriented-programming/) |
| Files and error handling | Planned | [File processing](03-files-and-errors/) |
| Basic projects | Planned | [Larger applications](04-basic-projects/) |
| Engineering simulations | Planned | [Device and sensor scenarios](05-engineering-simulations/) |

[View the full exercise and project roadmap](ROADMAP.md).

## Development approach

I write my own first attempt, use AI-assisted explanations and code review to understand mistakes, and revise the implementation. Each completed exercise includes a runnable program and documentation of its behavior.

The documented checks are manual input/output cases; an automated test suite and continuous integration are not yet part of this portfolio.

## License

[MIT](LICENSE)
