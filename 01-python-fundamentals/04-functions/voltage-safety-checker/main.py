"""Classify simulated voltage readings against defined operating ranges."""

import math


def is_valid_voltage(voltage):
    return math.isfinite(voltage) and voltage >= 0


def classify_voltage(voltage):
    if 0 <= voltage < 3.0:
        return "LOW"
    elif 3.0 <= voltage <= 3.6:
        return "NORMAL"
    else:
        return "HIGH"


def main():
    while True:
        try:
            user_input = input(
                "Enter voltage in V or 'done': ").strip().lower()
            if user_input == 'done':
                print("Goodbye!")
                break
            voltage = float(user_input)
            if is_valid_voltage(voltage):
                status = classify_voltage(voltage)
                print(f"Voltage: {voltage:.2f} V | Status: {status}")
            else:
                print("Invalid voltage: enter a finite value of 0 V or above.")
        except ValueError:
            print("Invalid input: enter a number or 'done'.")
            continue


if __name__ == "__main__":
    main()
