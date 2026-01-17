# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.
def calculate_average_order_value(orders):
    total = 0.0
    count = 0

    for order in orders:
        if order.get("status") != "cancelled":
            try:
                total += float(order["amount"])
                count += 1
            except (KeyError, TypeError, ValueError):
                continue

    return total / count if count > 0 else 0.0
