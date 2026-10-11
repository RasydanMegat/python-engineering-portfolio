# Component Inventory

A command-line Python program for managing the quantities of three simulated electronic components: RESISTOR, CAPACITOR, and LED. It uses a dictionary to keep only components with stock greater than zero.

## Features

- Add or remove component stock using positive whole-number quantities.
- Show components in the order they were added, along with the total units in stock.
- Reject unsupported components and invalid quantities without changing inventory.
- Prevent removals that exceed available stock.
- Delete a component when its quantity reaches zero. If added again, it appears at the end of the display order.

This is an educational simulation; it does not use a database or connect to hardware.

## Run

Requires Python 3.7 or later. No additional packages are needed. From this folder, run:

```text
python main.py
```

On Windows, use `py main.py` if `python` is unavailable.

## Example

```text
Action (add/remove/show/done): add
Component (RESISTOR/CAPACITOR/LED): resistor
Quantity: 5
Added 5 to RESISTOR.
Action (add/remove/show/done): add
Component (RESISTOR/CAPACITOR/LED): led
Quantity: 2
Added 2 to LED.
Action (add/remove/show/done): show
Component inventory
RESISTOR: 5
LED: 2
Total units: 7
Action (add/remove/show/done): remove
Component (RESISTOR/CAPACITOR/LED): RESISTOR
Quantity: 3
Removed 3 from RESISTOR.
Action (add/remove/show/done): show
Component inventory
RESISTOR: 2
LED: 2
Total units: 4
Action (add/remove/show/done): done
```

An empty inventory displays `Inventory is empty.` A request for more stock than is available displays a message such as `Not enough stock for LED.` and leaves inventory unchanged.

## How it works

`add_stock()` changes the existing dictionary using `.get(component, 0)` to treat a new component as having zero stock. `remove_stock()` returns `False` when stock is insufficient; otherwise it updates or deletes the component and returns `True`. `display_inventory()` uses `.items()` to display component/quantity pairs and `sum(inventory.values())` to calculate total units. `main()` handles the menu and validates input before calling these functions.

## Verification

The following input/output cases passed during review. They are documented checks, not a committed automated test suite.

| Scenario | Result |
| --- | --- |
| Show immediately | Empty-inventory message |
| Add LED 4 | LED: 4; total units 4 |
| Add RESISTOR 5, then 2 more | RESISTOR: 7; one component line |
| Add LED 3, remove 2 | LED: 1 |
| Add LED 3, remove 3 | LED deleted; empty inventory |
| Remove LED from empty inventory | Not-enough-stock message; no change |
| Add LED 2, try to remove 3 | Not-enough-stock message; LED remains 2 |
| Delete and re-add RESISTOR after adding LED | LED appears before RESISTOR |
| Unsupported component | Rejected before quantity prompt |
| Invalid quantities: 0, -2, 2.5, text | Rejected without stock changes |
| Mixed-case actions with surrounding spaces | Accepted |

Helper checks confirmed that `add_stock()` changes the original dictionary and `remove_stock()` returns the correct Boolean without making stock negative.

## Learning process

I made an initial implementation, reviewed the control-flow errors, and studied an AI-assisted working example before using it for the final program. The behavior was verified with the cases above.

## Files

- `main.py`: completed program
- `README.md`: usage, behavior, and verification cases

[Data structures](../../README.md) · [Learning roadmap](../../../ROADMAP.md)
