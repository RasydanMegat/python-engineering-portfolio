"""Rank simulated error-code frequencies and report every most common code."""


VALID_CODES = ("E01", "E02", "E03")


def record_error(counts, code):
    counts[code] = counts.get(code, 0) + 1


def rank_errors(counts):
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return ranked


def find_most_common(counts):
    # An empty dictionary has no highest frequency.
    if not counts:
        return []

    highest_frequency = max(counts.values())
    common_codes = []

    # Include every code tied for the highest frequency.
    for code, frequency in counts.items():
        if frequency == highest_frequency:
            common_codes.append(code)

    return sorted(common_codes)


def display_report(counts):

    if len(counts) == 0:
        print("No valid error codes entered.")
        return

    print("Error frequency ranking")
    print(f"Total reports: {sum(counts.values())}")
    print(f"Unique codes: {len(counts)}")
    print("Rankings:")

    ranked = rank_errors(counts)

    for rank, (code, total) in enumerate(ranked, start=1):
        print(f"{rank}. {code} - {total}")

    common_codes = find_most_common(counts)
    highest_frequency = max(counts.values())

    print(f"Most common codes: {', '.join(common_codes)}")
    print(f"Highest frequency: {highest_frequency}")


def main():
    counts = {}

    while True:
        code = input(
            "Enter error code (E01/E02/E03) or 'done': ").strip().upper()

        if code == "DONE":
            break

        if code not in VALID_CODES:
            print("Invalid code: enter E01, E02, E03, or 'done'.")
            continue
        else:
            record_error(counts, code)

    display_report(counts)


if __name__ == "__main__":
    main()
