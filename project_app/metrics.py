"""Small statistical helper functions for the analytics-agent demo."""

from collections.abc import Iterable


def average(values: Iterable[float]) -> float:
    """Return the arithmetic mean of a non-empty collection of numbers."""
    values_list = list(values)

    if not values_list:
        raise ValueError("average requires at least one value")

    return sum(values_list) / len(values_list)


def median(values: Iterable[float]) -> float:
    """Return the median of a non-empty collection of numbers.

    For odd-length collections, returns the middle value.
    For even-length collections, returns the average of the two middle values.
    """
    values_list = list(values)

    if not values_list:
        raise ValueError("median requires at least one value")

    sorted_values = sorted(values_list)
    n = len(sorted_values)

    if n % 2 == 1:
        return sorted_values[n // 2]
    else:
        mid1 = sorted_values[n // 2 - 1]
        mid2 = sorted_values[n // 2]
        return (mid1 + mid2) / 2


def summarize_range(values: Iterable[float]) -> dict[str, float]:
    """Return the minimum and maximum values from a non-empty collection.

    Returns a dictionary with 'min' and 'max' keys.
    """
    values_list = list(values)

    if not values_list:
        raise ValueError("summarize_range requires at least one value")

    return {"min": min(values_list), "max": max(values_list)}
