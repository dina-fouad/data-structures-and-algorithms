 # define a class called Node
class Node:
  def __init__(self, value=""):
    self.value = value
    self.next = None


# define a class called Linked List
class LinkedList():
  def __init__(self):
    self.head = None
    self.values=[]

  def insert(self, value):
    """ Add a new node containing the given value to the head of the LinkedList """

    node = Node(value)

    if self.head:
      node.next = self.head

    self.head = node

  def __str__(self):
    string = ""
    current = self.head

    while current:
      string += f"{str(current.value)} -> "
      current = current.next
    string += "None"
    return string


  def includes(self, key):

        current = self.head
        while current.value is not None:
            if current.value == key:

                return True
        else :
            current = current.next
        return False

if __name__ == "__main__":
  ll = LinkedList()
  ll.insert(5)
  ll.insert(4)
  print(ll)
  node1 =  Node(1)
  node2 =  Node(2)
  node3 = node1 + node2
  print(node3)

  for value in ll:
    print(value)
