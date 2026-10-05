# Object-Oriented Programming

Planned Python exercises and projects for modelling devices, state, and behaviour with classes and objects. **Status: not started.**

## When to start

Finish the remaining fundamentals exercises, then practise lists and dictionaries. Begin the first four OOP exercises once functions and these collections feel comfortable. Complete the file-handling stage before projects that save or load data.

Suggested order: fundamentals -> data structures -> OOP exercises -> file handling -> OOP projects.

This folder is numbered `06` to preserve existing portfolio paths; the number does not require completing every simulation before learning OOP.

## Learning objectives

- Explain the difference between a class and an object.
- Use `__init__`, `self`, instance attributes and methods.
- Keep each object's state independent.
- Validate changes to an object's state.
- Combine objects through composition.
- Use inheritance and polymorphism when they make the design clearer.
- Test behaviour and explain when a function is sufficient.

## Exercise sequence

All entries below are planned. Exercise folders and detailed starter instructions will be added one at a time.

| # | Exercise | Concepts | Completion target |
| --- | --- | --- | --- |
| 1 | Device Profile | Classes, objects, `__init__`, `self`, attributes | Create two devices with separate names and IDs; changing one must not change the other. |
| 2 | Temperature Sensor | Methods, parameters, return values, instance state | Store a reading and return its low/normal/high category using exercise-defined thresholds; keep printing outside the calculation method. |
| 3 | Battery Model | Validation and controlled state changes | Charge and discharge a simulated battery within 0-100%; reject invalid operations without changing its state. |
| 4 | Device Registry | Lists/dictionaries of objects | Add, find and remove devices by ID; reject duplicate IDs and handle missing devices. |
| 5 | Monitoring Station | Composition: one object contains other objects | Give a station multiple sensors and produce a summary using their methods; handle an empty station. |
| 6 | Sensor Types | Simple inheritance and `super()` | Share an ID and unit through a base sensor class, then specialise temperature and voltage sensors. |
| 7 | Common Sensor Interface | Polymorphism | Process different sensor objects through the same method name without a separate type-check branch for each one. |
| 8 | Testable Device State | `__repr__`, modules and `unittest` | Provide useful object representations and automated tests for state changes, boundaries and independent instances. |

## Planned projects

### 1. Equipment Inventory Manager

A command-line application using `Equipment` objects and an `Inventory` class.

- Add, search, update and remove equipment by unique ID.
- Validate IDs and allowed status values.
- Save and load records in JSON after completing file-handling practice.
- Handle malformed files and missing records.
- Include tests, a sample data file, usage instructions and a short class-design explanation.

### 2. Sensor Monitoring Station Simulator

A simulation using sensor objects and a monitoring station that contains them.

- Support at least temperature and voltage sensor types.
- Accept simulated readings and return status summaries through a common interface.
- Configure thresholds explicitly for the exercise.
- Handle empty input and invalid readings.
- Test each sensor's behaviour and the combined station summary.

### 3. Battery-Powered Device Simulator

A simulation combining `Battery` and `Device` objects.

- Model device states such as off, idle and active.
- Define charge consumption per simulated step.
- Prevent impossible charge levels and invalid state transitions.
- Record a session summary and test transition boundaries.
- Explain why composition fits this design.

The sensor and battery examples are educational software models. Their thresholds and behaviour are exercise rules, not specifications for real hardware.

## What every completed exercise should include

- A clear problem statement, expected behaviour and acceptance cases.
- An initial implementation written before reviewing a reference answer.
- Review feedback and corrections the learner can explain.
- A completed program and README with sample runs.
- Automated tests once testing has been introduced.

Completed projects should also explain which object owns each piece of state, why classes were useful, and which parts remain ordinary functions. Use inheritance only where there is a meaningful shared relationship.

## Connection to the wider portfolio

These exercises provide Python practice in organizing state and behaviour. Later C/C++ and hardware work will require additional language, memory, timing and device-specific knowledge.

[Full roadmap](../ROADMAP.md) · [Portfolio overview](../README.md)
