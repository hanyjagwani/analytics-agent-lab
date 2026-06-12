"""Small statistical helper functions for the analytics-agent demo."""

from collections.abc import Iterable


def average(values: Iterable[float]) -> float:
    """Return the arithmetic mean of a non-empty collection of numbers."""
    values_list = list(values)

    if not values_list:
        raise ValueError("average requires at least one value")

    return sum(values_list) / len(values_list)
