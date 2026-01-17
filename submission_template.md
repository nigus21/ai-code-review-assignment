# AI Code Review Assignment (Python)

## Candidate
- Name: Nigus Dibekulu
- Approximate time spent: 1 hour

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- The divisor uses the total number of orders, including cancelled ones, while the numerator excludes them, resulting in an incorrect average.

- Division by zero occurs when the input list is empty.

### Edge cases & risks
- All orders are cancelled, leading to division by zero.
- Missing "status" or "amount" keys can raise exceptions.
- Non-numeric or malformed "amount" values can cause runtime errors.

### Code quality / design issues
- Implicit assumptions about input structure and data types.
- Lack of defensive checks makes the function unsafe for real-world data.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Track only non-cancelled orders when computing the average.
- Guard against division by zero.
- Add minimal validation for missing or invalid order data.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

- Empty input lists to ensure safe handling.
- Mixed cancelled and non-cancelled orders to verify correct averaging.
- Inputs with missing keys or invalid amount values to confirm robustness.
- Cases where all orders are cancelled to ensure no division-by-zero errors.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- It incorrectly claims cancelled orders are excluded from the calculation, while they are still included in the divisor.

- It does not mention failure cases such as empty input or invalid data.

### Rewritten explanation
- This function calculates the average value of non-cancelled orders by summing their amounts and dividing by the count of valid, non-cancelled orders. It safely handles empty inputs and invalid data by returning 0.0 when no valid orders are present.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The original code’s intent is reasonable, but it contains a critical mathematical error and unsafe assumptions that must be corrected before use.
- Confidence & unknowns: High confidence in the corrected logic. Business rules for handling missing status values could vary depending on domain requirements.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- The check "@" in email is not sufficient to determine whether an email is valid.
- The function will raise a TypeError if email is None or not a string.

### Edge cases & risks
- Strings like "@", "test@", or "@example" are counted as valid but are not valid email addresses.
- Non-string values in the list cause runtime errors.
- Leading/trailing whitespace is not handled.

### Code quality / design issues
- The implementation overclaims correctness compared to what it actually validates.
- No input validation or type checking is performed.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Add type checking to safely ignore non-string inputs.

- Use minimal structural validation for email format.

- Keep the logic intentionally simple and readable.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- Valid email formats (e.g., user@example.com) to ensure they are correctly counted.
- Clearly invalid formats (e.g., "@", "test@", "@example.com") to confirm they are excluded.
- Non-string inputs such as None, integers, or objects to verify safe handling without errors.
- Empty input lists to confirm the function returns zero without failure.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- Claims the function validates email addresses, which it does not.

- Incorrectly states that invalid entries are safely ignored.

- Overstates correctness and robustness.

### Rewritten explanation
- This function counts email addresses that meet basic structural criteria, such as containing a local part and a domain with a dot. It safely ignores non-string and malformed inputs but does not perform full RFC-compliant email validation.

## 4) Final Judgment
- Decision: Reject

- Justification: The original implementation does not meet its stated goal of validating email addresses and fails on common edge cases.

- Confidence & unknowns: High confidence in the corrected logic. Full email validation rules may vary depending on application requirements.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- The divisor count = len(values) includes None values, so the average is incorrect if there are missing measurements.
- Non-numeric or invalid entries (strings, objects) will cause a runtime error when calling float(v).

### Edge cases & risks
- Empty input list → total / 0 → division by zero.
- All values are None → division by zero.
- Mixed types (int, float, string, None) not safely handled.

### Code quality / design issues
- Assumes every non-None value can be converted to float.

- Explanation overclaims safety: the function does not handle all mixed input types safely.

- No defensive programming is applied.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Count only valid numeric values in the divisor.

- Safely ignore None and non-numeric values.

- Guard against division by zero by returning 0.0 when no valid measurements exist.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- A list with integers and floats to ensure correct averaging.
- A list containing None values to verify they are ignored.
- A list with invalid types (strings, objects) to confirm safe handling.
- An empty list to verify zero is returned.
- A list where all values are None to ensure no division-by-zero occurs.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- Incorrectly states that all mixed types are safely handled.

- Divides by the total length instead of the count of valid measurements, which is mathematically incorrect.

- Fails to mention division-by-zero edge cases.

### Rewritten explanation
- This function calculates the average of valid numeric measurements by ignoring None and non-numeric values. It returns 0.0 if no valid measurements exist and ensures a safe, correct average.

## 4) Final Judgment
- Decision: Reject
- Justification: The original implementation divides by the total number of input values rather than the count of valid measurements, leading to incorrect results. It also crashes on non-numeric types.
- Confidence & unknowns: High confidence in corrected logic. Edge case handling is safe, but domain rules for what counts as “valid measurement” could vary.
