"""Collect equipment scores and rank them by score, then by name."""


def sort_results(results):
    ranked = sorted(results.items(), key=lambda item: (-item[1], item[0]))
    return ranked


def display_report(results):
    if len(results) == 0:
        print("No equipment results entered.")
        return

    print("Equipment results")
    print(f"Total equipment: {len(results)}")
    print("Rankings:")

    ranked = sort_results(results)

    for rank, (name, score) in enumerate(ranked, start=1):
        print(f"{rank}. {name} - {score}")


def main():
    results = {}

    while True:
        name = input("Equipment name or 'done': ").strip().upper()

        if name == "DONE":
            break

        if not name:
            print("Invalid equipment name: enter a name or 'done'.")
            continue

        if name in results:
            print(f"Duplicate equipment: {name}.")
            continue

        score_user = input("Score (0-100): ")

        try:
            score = int(score_user)
            if 0 <= score <= 100:
                results[name] = score
            else:
                print("Invalid score: enter a whole number from 0 to 100.")
                continue
        except ValueError:
            print("Invalid score: enter a whole number from 0 to 100.")
            continue

    display_report(results)


if __name__ == "__main__":
    main()
