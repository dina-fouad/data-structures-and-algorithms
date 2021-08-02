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
        current=self.head
        length=1
        while current.next:
            length+=1
            current=current.next
        current=self.head
        if k>= length:
            return 'Error! index out of range'
        elif k<0:
            return "Error! k can't be negative number"
        else:
            count =length-k-1
            for i in range(length):
                    if i == count:
                        return current.value
                    current =current.next

def kth(self,j):
        current=self.head
        val=[]
        while current:
            val+=[current.value]
            current=current.next
        val=val[::-1]

        for i in range(len(val)):
            if i==j:
                return val[j]
