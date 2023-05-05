import pytest
from Lab2a import find_min_max, calc_median_temperature, calc_average

# Test for find_min_max() function
def test_find_min_max():
    assert find_min_max([1, 2, 3, 4, 5]) == (1, 5)
    assert find_min_max([10, 2, 3, 4, 1]) == (1, 10)
    assert find_min_max([0]) == (0, 0)

# Test for calc_average() function
def test_calc_average():
    assert calc_average([1, 2, 3, 4, 5]) == 3.0
    assert calc_average([10, 20, 30, 40, 50]) == 30.0
    assert calc_average([0]) == 0.0

# Test for calc_median_temperature() function
def test_calc_median_temperature():
    assert calc_median_temperature([1, 2, 3, 4, 5]) == 3.0
    assert calc_median_temperature([10, 20, 30, 40, 50, 60]) == 35.0
    assert calc_median_temperature([0]) == 0.0
