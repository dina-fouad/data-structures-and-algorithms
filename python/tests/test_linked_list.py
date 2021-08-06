
import pytest



from linked_list.linked_list import LinkedList,Node

def test_instance(): ## 1 ## 1
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert isinstance(ll, LinkedList)

def test_insert():
    l1=LinkedList()
    value=100
    l1.insert(value)
    actual1=l1.head.value
    actual2=l1.head.next
    excepted1=100
    excepted2=None
    assert actual1==excepted1
    assert actual2==excepted2

def test_head():
    l1=LinkedList()
    node1=l1.insert('200')
    assert l1.head.value=='200'



def test_fisrt_elment(): 
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.head.value == 3

def test_false_value():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.includes(5) == False

def test_true():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.includes(2) == True

def test_str():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.__str__() == "{'3'} ->{'2'} ->{'1'} ->"


