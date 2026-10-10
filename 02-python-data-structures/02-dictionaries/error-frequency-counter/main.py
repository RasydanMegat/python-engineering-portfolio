"""Count valid simulated error codes and display a frequency report."""


def record_error(counts, code):
    # Increase the count for one valid error code
    counts[code] = counts.get(code, 0) + 1


def display_report(counts):
    if not counts:
        print("No valid error codes entered.")
        return

    print("Error frequency report")
    print(f"Total reports: {sum(counts.values())}")
    print(f"Unique codes: {len(counts)}")
    print("Counts:")

    for code, frequency in counts.items():
        print(f"{code}: {frequency}")


def main():
    counts = dict()

    while True:
        code = input(
            "Enter error code (E01/E02/E03) or 'done': ").strip().upper()

        if code == 'DONE':
            break

        if code not in ("E01", "E02", "E03"):
            print("Invalid code: enter E01, E02, E03, or 'done'.")
            continue

        record_error(counts, code)

    display_report(counts)


if __name__ == "__main__":
    main()
