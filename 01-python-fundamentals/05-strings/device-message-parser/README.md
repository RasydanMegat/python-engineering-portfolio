# Device Message Parser

A command-line Python program that parses a simulated device message in the format `DEVICE_ID:STATUS`, validates its fields, and displays a readable status summary.

## Features

- Requires exactly one colon separator.
- Extracts fields using string slicing.
- Removes surrounding whitespace while preserving device ID capitalisation and internal spaces.
- Normalises status to uppercase and accepts only `ON`, `OFF`, or `ERROR`.
- Rejects missing fields and unsupported statuses.
- Stops on invalid input without displaying a partial summary.

This is an educational message format. The program does not communicate with physical devices.

## Requirements and usage

Python 3.6 or later. No additional packages are required.

From this folder, run:

```text
python main.py
```

On Windows, use `py main.py` if `python` is unavailable. Each run accepts one message.

## Examples

```text
Enter device message: MOTOR_01:ON
Device ID: MOTOR_01
Status: ON
Description: Device is running.
```

```text
Enter device message:   Fan_02 : off
Device ID: Fan_02
Status: OFF
Description: Device is stopped.
```

```text
Enter device message: SENSOR_03:Error
Device ID: SENSOR_03
Status: ERROR
Description: Device needs attention.
```

```text
Enter device message: MOTOR_01:READY
Invalid status: use ON, OFF, or ERROR
```

## Validation order

The program checks separator count, device ID, status presence, and allowed status in that order. It prints only the first applicable error:

| Condition | Message |
| --- | --- |
| Missing or multiple colons | `Invalid format: use DEVICE_ID:STATUS with exactly one colon` |
| Empty device ID after trimming | `Invalid device ID: cannot be empty` |
| Empty status after trimming | `Invalid status: cannot be empty` |
| Unsupported status | `Invalid status: use ON, OFF, or ERROR` |

A device ID may contain spaces or digits; this exercise imposes no further ID restrictions. Internal spaces within a status are preserved, so `O N` is invalid.

## Functions

| Function | Responsibility |
| --- | --- |
| `get_device_id(message)` | Return the trimmed string before the colon |
| `get_device_status(message)` | Return the trimmed, uppercase string after the colon |
| `main()` | Validate the message, select a description, and display the summary |

Both helpers assume there is exactly one colon, checked by `main()` before they are called. They return strings and leave printing to `main()`.

## Verification cases

The following 17 input/output cases and 12 helper-function checks passed during review. These are documented checks, not a committed automated test suite.

| Input | Expected result |
| --- | --- |
| `MOTOR_01:ON` | ID `MOTOR_01`, status `ON`, running description |
| `Fan_02:off` | ID `Fan_02`, status `OFF`, stopped description |
| `SENSOR_03:Error` | ID `SENSOR_03`, status `ERROR`, attention description |
| `  Motor_01 : on  ` | ID `Motor_01`, status `ON`, running description |
| `Fan A:OFF` | Internal ID space preserved |
| `404:ON` | Numeric ID preserved as text |
| Empty input | Invalid format |
| Whitespace only | Invalid format |
| `MOTOR_01` | Invalid format |
| `MOTOR_01:ON:EXTRA` | Invalid format |
| `:ON` | Empty device ID |
| `MOTOR_01:` | Empty status |
| `   : ON` | Empty device ID |
| `MOTOR_01:   ` | Empty status |
| `:` | Empty device ID, checked first |
| `MOTOR_01:READY` | Unsupported status |
| `MOTOR_01:O N` | Unsupported status |

All valid cases display the device ID, status and description. Invalid cases exit without a partial summary.

## Skills practised

String slicing, separator counting, whitespace handling, case normalisation, function return values, early returns, and conditional output.

The first slice stops before the colon. The second starts one character after it, excluding the separator from both extracted values.

## Files

- `main.py`: completed program
- `README.md`: usage, validation rules, and verification cases

[Fundamentals](../../README.md) · [Learning roadmap](../../../ROADMAP.md)
