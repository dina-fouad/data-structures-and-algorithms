import pytest
from stack_and_queue import  PseudoQueue, Queue, Stack, Node, StackEmptyException



def test_tests():

  assert 1 == 1


@pytest.fixture
def data():
  new_stack = Stack()

  return {'stack':new_stack}



def test_stack_pushing_one_element(data):
  data['stack'].push(1)
  actual = data['stack'].top.value
  expected = 1
  assert actual == expected

def test_stack_push_multiple():


    stack = Stack()
    assert stack.top == None
    stack.push(5)
    assert stack.top.value == 5
    stack.push(1)
    assert stack.top.value == 1
    stack.push(2)
    assert stack.top.value == 2




def test_stack_pop_multiple(data):
    data['stack'].push(1)
    data['stack'].push(2)
    actual = data['stack'].pop()
    expected = 2
    assert expected == actual

def test_empty_after():
  Stack =Stack()
  Stack.push(1)
  Stack.push(2)
  Stack.pop()
  Stack.pop()
  assert Stack.top==None


def test_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2

def test_create_empty_stack():
    stack = Stack()
    assert stack.top == None


def test_peek_empty_stack_exception():
    stack = Stack()
    actual = stack.peek()
    expected = "empty stack"
    assert actual == expected

def test_enqueue_from_queue():
    queue = Queue()
    queue.enqueue(1)
    actual = queue.front.value
    expected = 1
    assert actual == expected

def test_queue_enqueue_while_two_node():
  queue=Queue()
  queue.enqueue(1)
  queue.enqueue(2)
  queue.enqueue(3)
  queue.dequeue()
  assert queue.front.value==2


def test_queue_dequeue():
    queue = Queue()
    queue.dequeue()
    assert queue.peek() == "Queue is empty"

def test_queue_peek():
    queue = Queue()
    queue.enqueue(1)
    assert queue.peek() == 1

def test_instantiate_queue():

    queue = Queue()
    assert queue

def test_peek_empty_queue_exception():

    queue = Queue()
    actual = queue.peek()
    expected = "Queue is empty"
    assert actual == expected
#############################################################




def queue_vals():
    queue = PseudoQueue()
    queue.enqueue(8)
    queue.enqueue('hi')
    queue.enqueue(-4)
    queue.enqueue(6)
    return queue

def test_empty_queue():
    queue=PseudoQueue()
    expected = "can't dequeue from empty stack "
    actual =queue.dequeue()
    assert actual == expected

