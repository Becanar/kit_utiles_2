from src.numbers import unique_sorted

def test_unique_sorted_with_numbers():
  
    seq = [3, 1, 2, 3, 2]

    result = unique_sorted(seq)

    assert result == [1, 2, 3]


def test_unique_sorted_with_strings():

    seq = ["b", "a", "b"]

    result = unique_sorted(seq)

    assert result == ["a", "b"]
