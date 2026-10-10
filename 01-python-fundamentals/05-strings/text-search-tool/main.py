"""Search text without case sensitivity and report match counts and positions."""


def count_occurrences(text, keyword):
    """Return the number of non-overlapping matches, ignoring letter case."""
    text = text.lower()
    keyword = keyword.lower()
    return text.count(keyword)


def find_first_occurrence(text, keyword):
    """Return the first matching index, or -1 if there is no match."""
    text = text.lower()
    keyword = keyword.lower()
    return text.find(keyword)


def main():

    text = input("Enter text:").strip()

    if not text:
        print("You did not enter any text.")
        return

    keyword = input("Enter keyword:").strip()

    if not keyword:
        print("You did not enter any keyword.")
        return

    count = count_occurrences(text, keyword)
    first_index = find_first_occurrence(text, keyword)

    print(f"Text: {text}")
    print(f"Keyword: {keyword}")
    print(f"Number of matches: {count}")

    if first_index == -1:
        print("No match found.")
    else:
        print(f"First match position: {first_index}")


if __name__ == "__main__":
    main()
