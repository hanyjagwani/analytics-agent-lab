# Task Completion Report

## Selected Task
- **ID**: METRICS-001
- **Title**: Add a median helper function

## Files Changed
- `project_app/metrics.py` - Added `median()` function
- `tests/test_metrics.py` - Added 6 focused test cases

## Summary
Implemented a `median()` helper function that calculates the median value of a collection. The function:
- Returns the middle value for odd-length collections
- Returns the average of the two middle values for even-length collections
- Rejects empty collections with a clear `ValueError`
- Handles both integer and decimal values
- Works with unsorted input by sorting internally

## Test Coverage
Added focused tests covering:
- `test_median_returns_middle_value_for_odd_length()` - Verifies odd-length behavior
- `test_median_returns_average_of_two_middle_values_for_even_length()` - Verifies even-length behavior
- `test_median_works_with_single_value()` - Edge case with one element
- `test_median_works_with_decimal_values()` - Decimal value support
- `test_median_works_with_unsorted_input()` - Verifies sorting behavior
- `test_median_rejects_empty_input()` - Verifies error handling for empty collections

## Review Notes
The implementation follows the existing code style and patterns used in the `average()` function. All acceptance criteria from the backlog have been met:
- ✓ Added median function to project_app/metrics.py
- ✓ Supports odd-length and even-length collections
- ✓ Rejects empty collection with clear ValueError
- ✓ Added focused tests in tests/test_metrics.py
