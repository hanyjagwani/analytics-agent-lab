import pytest

from project_app.metrics import average


def test_average_returns_arithmetic_mean() -> None:
    assert average([2, 4, 6]) == 4


def test_average_accepts_decimal_values() -> None:
    assert average([1.5, 2.5]) == 2


def test_average_rejects_empty_input() -> None:
    with pytest.raises(ValueError, match="at least one value"):
        average([])
