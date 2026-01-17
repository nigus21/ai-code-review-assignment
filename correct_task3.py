# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.
def average_valid_measurements(values):

    total = 0.0
    count = 0

    for value in values:
        if value is None:
            continue
        try:
            total += float(value)
            count += 1
        except (TypeError, ValueError):
            continue

    return total / count if count > 0 else 0.0
