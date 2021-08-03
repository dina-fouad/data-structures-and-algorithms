
import pytest



from linked_list.linked_list import LinkedList,Node


# test creating a linked list
def test_linkedlist():
   assert LinkedList()




def test_includes_method():
    list = LinkedList()
    list.insert(17)
    assert list.head.value == 17

def test__str__():
    list = LinkedList()
    list.insert('c')
    list.insert('b')
    list.insert('a')
    actual = list.__str__()
    expected = "{ a } -> { b } -> { c } -> NULL"
    assert actual == expected


######## code challange 6 ##########

def test_append():
    test=LinkedList()
    test.insert(40)
    test.insert(50)
    test.insert(49)
    test.appendList(90)
    expected="49 -> 50 -> 40 -> 90 -> NULL"
    actual=test.__str__()
    assert actual==expected

def test_append_mid():
    test=LinkedList()
    test.insert(40)
    test.insert(50)
    test.insert(49)
    test.appendList(90)
    test.appendList(100)
    expected="49 -> 50 -> 40 -> 90 -> 100 -> NULL"
    actual=test.__str__()
    assert actual==expected


def test_insertBefore():
    test=LinkedList()
    test.insert(40)
    test.insert(50)
    test.insert(49)
    test.insertBefore(40,50)
    expected="49 -> 50 -> 40 -> 90 -> NULL"
    actual=test.__str__()
    assert actual==expected

def test_insertBefore_first():
    test=LinkedList()
    test.insert(40)
    test.insert(50)
    test.insert(49)
    test.insertBefore(49,30)
    expected="30 -> 49 -> 50 -> 40 -> 90 -> NULL"
    actual=test.__str__()
    assert actual==expected

def test_insertAfter():
    test=LinkedList()
    test.insert(90)
    test.insert(50)
    test.insert(49)
    test.insertAfter(50,40)
    expected="49 -> 50 -> 40 -> 90 -> NULL"
    actual=test.__str__()
    assert actual==expected

def test_insertAfter_last():
    test=LinkedList()
    test.insert(90)
    test.insert(50)
    test.insert(49)
    test.insertAfter(40,90)
    expected="49 -> 50 -> 40 -> 90 -> NULL"
    actual=test.__str__()
    assert actual==expected

######## code challange 7 ##########
def test_k_greater_than_L_length():
    test =LinkedList()
    test.append(90)
    test.append(50)
    test.insert_after(90,30)
    excepted='Error! index out of range'
    actual=test.kthFromEnd(4)
    assert excepted==actual

def  test_k_the_same():
    test=LinkedList()
    test.append(90)
    test.append(50)
    test.insert_after(90,30)
    excepted='Error! index out of range'
    actual=test.kthFromEnd(3)
    assert excepted==actual
    ######## code challange 8 ##########


def test_linked_list_zipped_list():
    ll1= LinkedList()
    ll1.append(4)
    ll1.append(-1)
    ll1.append('s')
    ll1.insertBefore(4, 5)
    ll1.insertAfter(-1, 98)
    ll2= LinkedList()
    ll2.append(7)
    ll2.append(-8)
    ll2.insertAfter(7, 8)
    actual = str(zipLists(ll1,ll2))
    expected = "{5} ->{7} ->{4} ->{8} ->{-1} ->{-8} ->{98} ->{'s'} ->NULL"
    assert actual == expected  
