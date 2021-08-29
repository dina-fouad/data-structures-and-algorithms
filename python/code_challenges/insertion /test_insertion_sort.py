from insertion_sort import __version__
from insertion_sort import InsertionSort

def test_version():
    assert __version__ == '0.1.0'

def test_InsertionSort():
  arr1=[2,1,8,4,3]
  InsertionSort(arr1)
  assert [1,2,3,4,8]==arr1

  arr2=[8,4,23,42,16,15]
  InsertionSort(arr2)
  assert [4,8,15,16,23,42]==arr2
