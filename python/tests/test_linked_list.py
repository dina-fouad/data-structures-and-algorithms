
import pytest


from linked_list.linked_list import LinkedList , Node



# test creating a linked list
def test_linkedlist():
   assert LinkedList()


# test inserting values into linked list
def test_insert():
  # arrange
  ll = LinkedList()

  with pytest.raises(AttributeError):
    ll.head.value
  ll.insert(5)
  actual = ll.head.value
  assert actual == 5

# def test_includes_method():
#     list = LinkedList()
#     list.insert(17)
#     list.insert(6)
#     list.insert(93)
#     list.insert(5)
#     assert list.includes(6) == True
#     assert list.includes(3) == False

def test__str__():
    list = LinkedList()
    list.insert('c')
    list.insert('b')
    list.insert('a')
    actual = list.__str__()
    expected = "{ a } -> { b } -> { c } -> NULL"
    assert actual == expected


