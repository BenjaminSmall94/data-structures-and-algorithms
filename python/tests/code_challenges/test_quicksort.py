import pytest
from code_challenges.quicksort import quicksort


# @pytest.mark.skip("TODO")
def test_random():
    arr = [8, 4, 23, 42, 16, 15]
    actual = quicksort(arr, 0, len(arr) - 1)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_reverse():
    arr = [20, 18, 12, 8, 5, -2]
    actual = quicksort(arr, 0, len(arr) - 1)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_duplicates():
    arr = [5, 12, 7, 5, 5, 7]
    actual = quicksort(arr, 0, len(arr) - 1)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_nearly_sorted():
    arr = [2, 3, 5, 7, 13, 11]
    actual = quicksort(arr, 0, len(arr) - 1)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_one_element():
    arr = [1]
    actual = quicksort(arr, 0, len(arr) - 1)
    expected = [1]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_no_elements():
    arr = []
    actual = quicksort(arr, 0, len(arr) - 1)
    expected = []
    assert actual == expected
