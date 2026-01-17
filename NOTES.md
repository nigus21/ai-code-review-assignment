Notes

Assumptions

Task 1: Orders without "status" are treated as non-cancelled.

Task 2: uses a simple email check (local part + domain + dot).

Task 3: ignores non-numeric values safely.

Limitations

Task 1 does not check for negative amounts.

Task 2 uses basic validation, so very unusual invalid emails could pass.

Task 3 only handles ints/floats.

Alternatives Considered

Task 1: could raise errors for empty/missing fields, but returning 0.0 is safer.

Task 2: regex could improve validation but was more complex than needed.

Task 3: separate handling for invalid types, but try-except is concise and safe.
