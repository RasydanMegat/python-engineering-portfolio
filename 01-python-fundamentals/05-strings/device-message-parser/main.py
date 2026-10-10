"""Parse simulated device messages and display validated device status summaries."""


def get_device_id(message):
    """Return the trimmed text before the single colon, preserving its case."""
    # Assume main() has checked that there is exactly one colon.
    colon_index = message.find(":")
    device_id = message[:colon_index].strip()
    return device_id


def get_device_status(message):
    """Return the trimmed text after the single colon, in uppercase."""
    # Assume main() has checked that there is exactly one colon.
    colon_index = message.find(":")
    device_status = message[colon_index + 1:].strip().upper()
    return device_status


def main():

    message = input("Enter device message: ").strip()

    if message.count(":") != 1:
        print("Invalid format: use DEVICE_ID:STATUS with exactly one colon")
        return

    device_id = get_device_id(message)
    device_status = get_device_status(message)

    if not device_id:
        print("Invalid device ID: cannot be empty")
        return

    if not device_status:
        print("Invalid status: cannot be empty")
        return

    if device_status == "ON":
        description = "Device is running."

    elif device_status == "OFF":
        description = "Device is stopped."

    elif device_status == "ERROR":
        description = "Device needs attention."

    else:
        print("Invalid status: use ON, OFF, or ERROR")
        return

    print(f"Device ID: {device_id}")
    print(f"Status: {device_status}")
    print(f"Description: {description}")


if __name__ == "__main__":
    main()
