"""Collect production inspection results and report category counts and pass rate."""


def calculate_pass_rate(results):
    Pass_rate = (results.count("PASS") / len(results)) * 100
    return Pass_rate


def display_report(results):
    if len(results) == 0:
        print("No valid result entered.")
        return

    Total_items = len(results)
    Pass_count = results.count("PASS")
    Fail_count = results.count("FAIL")
    Rework_count = results.count("REWORK")
    Pass_rate = calculate_pass_rate(results)

    print("Recorded result")
    for number, result in enumerate(results, start=1):
        print(f"{number}. {result}")

    print("Production summary")
    print(f"Total items: {Total_items}")
    print(f"PASS count: {Pass_count}")
    print(f"FAIL count: {Fail_count}")
    print(f"REWORK count: {Rework_count}")
    print(f"Pass rate: {Pass_rate:.2f}%")


def main():
    results = list()

    while True:
        user_input = input(
            "Enter result (PASS/FAIL/REWORK) or 'done': ").strip().upper()

        if user_input == "DONE":
            break

        if user_input not in ("PASS", "FAIL", "REWORK"):
            print("Invalid result: enter PASS, FAIL, REWORK, or 'done'. ")
            continue
        else:
            results.append(user_input)

    display_report(results)


if __name__ == "__main__":
    main()
