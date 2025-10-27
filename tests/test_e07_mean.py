import pytest
from src.numbers import mean


def test_mean_valid_list():
    nums = [1, 2, 3, 4]

    result = mean(nums)

    assert result == 2.5


def test_mean_empty_list():

    nums = []

    with pytest.raises(ValueError, match="empty sequence"):
        mean(nums)
