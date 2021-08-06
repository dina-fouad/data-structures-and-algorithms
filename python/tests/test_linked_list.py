

from linked_list.linked_list import LinkedList,Node

def test_instance():
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


########################66666############################################

def test_append():
    l1=LinkedList()
    l1.append(10)
    assert l1.head.value is 10
    l1.append(20)
    assert l1.head.next.value is 20
    assert l1.head.next.next is None


def test_insert_before():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert_before(2,3)
    assert ll.__str__() == "{'3'} ->{'2'} ->{'1'} ->"

def test_insert_before_head():
    ll = LinkedList()
    ll.append(5)
    ll.append(6)
    ll.insert_before(5,4)
    assert ll.__str__() == "{'4'} ->{'5'} ->{'6'} ->"

def test_insert_after_last():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_after(3,4)
    assert ll.__str__() == "{'1'} ->{'2'} ->{'3'} ->{'4'} ->"

def test_insert_after():
    ll = LinkedList()
    ll.insert(5)
    ll.append(6)
    ll.insert_after(6,8)
    ll.insert(7)
    assert ll.__str__() == "{'7'} ->{'5'} ->{'6'} ->{'8'} ->"

    ########################77777############################################


def test_LinkedList_kth_from():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1)
    actual = ll.kth_from_end(0)
    expected = 2
    assert actual == expected

def test_LinkedList_kth():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1)
    actual = ll.kth_from_end(2)
    expected = 3
    assert actual == expected

def test_kth_negative():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    actual = ll.kth_from_end(-1)
    assert actual == 'Negative '

def test_linked_list_size_1():
    ll = LinkedList()
    ll.append(1)
    actual = ll.kth_from_end(1)
    expected = 1
    assert actual == expected

def test_happy():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    actual = ll.kth_from_end(2)
    expected = 1
    assert actual == expected
########################8888############################################
