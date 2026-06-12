import pytest

from project_app.metrics import average, median, summarize_range


def test_average_returns_arithmetic_mean() -> None:
    assert average([2, 4, 6]) == 4


def test_average_accepts_decimal_values() -> None:
    assert average([1.5, 2.5]) == 2


def test_average_rejects_empty_input() -> None:
    with pytest.raises(ValueError, match="at least one value"):
        average([])


def test_median_returns_middle_value_for_odd_length() -> None:
    assert median([3, 1, 5]) == 3


def test_median_returns_average_of_two_middle_values_for_even_length() -> None:
    assert median([1, 2, 3, 4]) == 2.5


def test_median_works_with_single_value() -> None:
    assert median([5]) == 5


def test_median_works_with_decimal_values() -> None:
    assert median([1.5, 2.5, 3.5]) == 2.5


def test_median_works_with_unsorted_input() -> None:
    assert median([5, 1, 3]) == 3


def test_median_rejects_empty_input() -> None:
    with pytest.raises(ValueError, match="at least one value"):
        median([])


def test_summarize_range_returns_min_and_max() -> None:
    result = summarize_range([1, 5, 3])
    assert result == {"min": 1, "max": 5}


def test_summarize_range_works_with_single_value() -> None:
    result = summarize_range([42])
    assert result == {"min": 42, "max": 42}


def test_summarize_range_works_with_decimal_values() -> None:
    result = summarize_range([1.5, 2.5, 3.5])
    assert result == {"min": 1.5, "max": 3.5}


def test_summarize_range_works_with_unsorted_input() -> None:
    result = summarize_range([5, 1, 3])
    assert result == {"min": 1, "max": 5}


def test_summarize_range_rejects_empty_input() -> None:
    with pytest.raises(ValueError, match="at least one value"):
        summarize_range([])
