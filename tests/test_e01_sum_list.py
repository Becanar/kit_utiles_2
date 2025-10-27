from src.numbers import sum_list

def test_sum_list_with_numbers():
   
    nums = [1, 2, 3, 4]

    result = sum_list(nums)

    assert result == 10


def test_sum_list_empty_list():
    
    nums = []

    result = sum_list(nums)

    assert result == 0
