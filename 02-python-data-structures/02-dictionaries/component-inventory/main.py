"""Manage a small simulated electronic-component inventory."""

VALID_COMPONENTS = ("RESISTOR", "CAPACITOR", "LED")


def add_stock(inventory, component, quantity):
    inventory[component] = inventory.get(component, 0) + quantity


def remove_stock(inventory, component, quantity):
    current_quantity = inventory.get(component, 0)

    if current_quantity < quantity:
        return False

    new_quantity = current_quantity - quantity

    if new_quantity == 0:
        del inventory[component]
    else:
        inventory[component] = new_quantity

    return True


def display_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
        return

    print("Component inventory")
    for component, quantity in inventory.items():
        print(f"{component}: {quantity}")
    print(f"Total units: {sum(inventory.values())}")


def main():
    inventory = {}

    while True:
        action = input("Action (add/remove/show/done): ").strip().lower()

        if action == "done":
            break

        if action == "show":
            display_inventory(inventory)
            continue

        if action not in ("add", "remove"):
            print("Invalid action: choose add, remove, show, or done.")
            continue

        component = input(
            "Component (RESISTOR/CAPACITOR/LED): "
        ).strip().upper()

        if component not in VALID_COMPONENTS:
            print("Invalid component: choose RESISTOR, CAPACITOR, or LED.")
            continue

        quantity_text = input("Quantity: ")

        try:
            quantity = int(quantity_text)
        except ValueError:
            print("Invalid quantity: enter a positive whole number.")
            continue

        if quantity <= 0:
            print("Invalid quantity: enter a positive whole number.")
            continue

        if action == "add":
            add_stock(inventory, component, quantity)
            print(f"Added {quantity} to {component}.")
        else:
            if remove_stock(inventory, component, quantity):
                print(f"Removed {quantity} from {component}.")
            else:
                print(f"Not enough stock for {component}.")


if __name__ == "__main__":
    main()
