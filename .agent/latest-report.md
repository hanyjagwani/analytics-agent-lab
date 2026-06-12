# Task Completion Report

## Selected Task
- **ID**: METRICS-002
- **Title**: Add a minimum and maximum summary helper

## Files Changed
- `project_app/metrics.py` - Added `summarize_range()` function
- `tests/test_metrics.py` - Added import for `summarize_range` and 5 focused tests

## Summary
Implemented the `summarize_range(values)` function that returns a dictionary with `min` and `max` keys containing the minimum and maximum values from a non-empty collection. The function raises a clear `ValueError` when given an empty collection.

## Test Coverage
Added 5 focused tests covering:
- `test_summarize_range_returns_min_and_max()` - Basic min/max calculation
- `test_summarize_range_works_with_single_value()` - Single value edge case
- `test_summarize_range_works_with_decimal_values()` - Decimal values support
- `test_summarize_range_works_with_unsorted_input()` - Unsorted input handling
- `test_summarize_range_rejects_empty_input()` - Empty input rejection

## Review Notes
All acceptance criteria from the backlog have been met:
- ✓ Added a summarize_range function
- ✓ Returns the minimum and maximum values
- ✓ Rejects empty collection with clear ValueError
- ✓ Added focused tests in tests/test_metrics.py

The implementation follows the existing code style and error handling patterns consistent with `average()` and `median()` functions.
