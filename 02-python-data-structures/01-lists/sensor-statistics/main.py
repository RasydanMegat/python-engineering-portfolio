"""Collect finite temperature readings and display count, minimum, maximum, and average."""

import math


def calculate_average(readings):
    average = sum(readings) / len(readings)
    return average


def display_summary(readings):
    if len(readings) == 0:
        print("No valid readings entered.")
        return

    count = len(readings)
    lowest_reading = min(readings)
    highest_reading = max(readings)
    average = calculate_average(readings)

    print("Temperature summary")
    print(f"Reading count: {count}")
    print(f"Lowest temperature: {lowest_reading:.2f} C")
    print(f"Highest temperature: {highest_reading:.2f} C")
    print(f"Average temperature: {average:.2f} C")


def main():
    readings = list()

    while True:
        user_input = input("Enter temperature in C or 'done': ").strip()

        if user_input.lower() == "done":
            break

        try:
            temperature = float(user_input)
        except ValueError:
            print("Invalid input: enter a number or 'done'.")
            continue

        if not math.isfinite(temperature):
            print("Invalid temperature: enter a finite number.")

        else:
            readings.append(temperature)

    display_summary(readings)


if __name__ == "__main__":
    main()
