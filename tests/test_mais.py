import main

def test_sum_list():
    assert main.sum_list([1, 2, 3]) == 6
    assert main.sum_list([0, -1, 1]) == 0

def test_sort_list():
    assert main.sort_list([3, 1, 2]) == [1, 2, 3]

def test_apply_function():
    result = main.apply_function(lambda x: x * 2, [1, 2, 3])
    assert result == [2, 4, 6]

def test_multiplier_closure():
    times3 = main.multiplier(3)
    assert times3(4) == 12
    assert times3(0) == 0
