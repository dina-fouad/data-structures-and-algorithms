# define a class called Node
class Node:
  def __init__(self, value=""):
    self.value = value
    self.next = None


# define a class called Linked List
class LinkedList():
  def __init__(self):
    self.head = None


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
    else:
      string += "None"
    return string


  def includes(self, key):

        current = self.head
        while (current):

            if current.value == key:

                return True
        else :
            current = current.next
        return False

######## code challange 6 ##########

  def appendList(self, value):
        new_node = Node(value)
        current = self.head
        if current == None:
           current = new_node
        else:
            while current.next != None:
                current = current.next
        current.next = new_node


def insertBefore(self,value,new_value):
        node = Node(new_value)
        current=self.head
        if current.value == value:
            self.insert(new_value)
        else :
            while current.next.value != value:
                  current=current.next
            else:
                node.next=current.next
                current.next=node



def insertAfter(self, value, new_value):
        current = self.head
        node = Node(new_value)
        while current != None:
            if current.value == value:
                break
            current = current.next
        node.next = current.next
        current.next = node

######## code challange 7 ##########


def kthFromEnd(self,k):

        if k<0:
            return "Can't enter negative input"
        list=[]
        current = self.head
        while current:
            list+=[current.value]
            current=current.next
        if k==0:
            return list[-1]
        else:
            if k>=len(list):
                return 'Exception'
            return list[(k*-1)-1]
######## code challange 8 ##########
def zipLists(test, test2):
    current1 = test.head
    current2 = test2.head
    while current1 and current2:
        save1 = current1.next
        save2 = current2.next

        current1.next = current2
        current2.next = save1

        current1 = save1
        current2 = save2

    return test
