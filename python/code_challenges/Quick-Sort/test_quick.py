import pytest
from quick import QuickSort

def test_quick_empty():
    assert QuickSort([], 0, len([])-1) == []

def test_quick_sorted():
    assert QuickSort([1,2,3,4,5], 0, len([1,2,3,4,5])-1) == [1,2,3,4,5]
