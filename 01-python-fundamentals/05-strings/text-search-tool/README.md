# Text Search Tool

A command-line Python program that searches text for a keyword without distinguishing uppercase and lowercase letters. It reports the number of non-overlapping matches and the position of the first match.

## Features

- Trims whitespace from both ends of the text and keyword.
- Rejects empty or whitespace-only input.
- Preserves original capitalisation when displaying the cleaned inputs.
- Counts substring matches, including matches within longer words.
- Reports the first zero-based position, or a clear no-match message.
- Separates search functions from user input and output.

## Requirements and usage

Python 3.6 or later. No additional packages are required.

From this folder, run:

```text
python main.py
```

On Windows, use `py main.py` if `python` is unavailable. Each run accepts one text and one keyword. There is no repeating menu or quit command.

## Examples

The prompts have no trailing space, so typed input appears immediately after the colon.

```text
Enter text:Error: motor error; ERROR cleared.
Enter keyword:error
Text: Error: motor error; ERROR cleared.
Keyword: error
Number of matches: 3
First match position: 0
```

```text
Enter text:All systems normal
Enter keyword:fault
Text: All systems normal
Keyword: fault
Number of matches: 0
No match found.
```

Empty text produces `You did not enter any text.` and exits before asking for a keyword. An empty keyword produces `You did not enter any keyword.` and exits without displaying results.

## Search behaviour

- Positions start at zero and refer to the cleaned text after whitespace trimming.
- Matches can occur inside words: `error` matches `errors`.
- Matches do not overlap: `ana` occurs once in `banana`.
- Spaces and punctuation inside the text are preserved.
- Numeric strings and multiword keywords are supported.
- The exercise is tested with ordinary English letters, digits and punctuation. Advanced Unicode case handling is outside its scope.

## Functions

| Function | Responsibility |
| --- | --- |
| `count_occurrences(text, keyword)` | Return a case-insensitive, non-overlapping match count |
| `find_first_occurrence(text, keyword)` | Return the first matching index, or `-1` if absent |
| `main()` | Validate input, call the helpers, and display results |

The helper functions expect non-empty, trimmed input from `main()`. They return values instead of printing them. `main()` converts the `-1` result into the user-facing no-match message.

## Verification cases

The following input/output cases were checked during review. They are documented checks, not a committed automated test suite.

| Text | Keyword | Count | First position or result |
| --- | --- | --- | --- |
| `Error: motor error; ERROR cleared.` | `error` | 3 | 0 |
| `Motor error` | `ERROR` | 1 | 6 |
| `All systems normal` | `fault` | 0 | No match found |
| `  Error cleared  ` | ` ERROR ` | 1 | 0 after trimming |
| `errors` | `error` | 1 | 0 |
| `banana` | `ana` | 1 | 1 |
| `error,error` | `error` | 2 | 0 |
| `Sensor ready; SENSOR READY` | `sensor ready` | 2 | 0 |
| `Error 404` | `404` | 1 | 6 |
| `OK` | `long keyword` | 0 | No match found |
| Empty text | Not requested | — | Text validation message |
| Whitespace-only text | Not requested | — | Text validation message |
| `Motor ready` | Empty | — | Keyword validation message |
| `Motor ready` | Whitespace only | — | Keyword validation message |

## Skills practised

String methods (`.strip()`, `.lower()`, `.count()`, `.find()`), return values, input validation, conditional output, and separating calculations from user interaction.

A first position of `0` is a valid match. Comparing explicitly with `-1` avoids treating zero as a failed search.

## Files

- `main.py`: completed program
- `README.md`: usage, behaviour, and verification cases

[Fundamentals](../../README.md) · [Learning roadmap](../../../ROADMAP.md)
