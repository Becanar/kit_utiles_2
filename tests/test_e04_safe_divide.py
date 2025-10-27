import pytest
from src.numbers import safe_divide


def test_safe_divide_valid():
    a, b = 10, 2

    result = safe_divide(a, b)

    assert result == 5


def test_safe_divide_division_by_zero():
  
    a, b = 10, 0

    with pytest.raises(ValueError, match="division by zero"):
        safe_divide(a, b)


def test_safe_divide_type_error():
  
    a, b = "3", 2

    with pytest.raises(TypeError, match="a and b must be numbers"):
        safe_divide(a, b)
