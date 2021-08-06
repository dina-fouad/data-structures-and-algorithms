class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():

    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        output = ''
        while current:
            output += f"{ {str(current.value)} } ->"
            current = current.next
        return output




    def insert(self, value):

        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self,value):

        current=self.head
        while current:
            if current.value==value:
                return True
            else :
                current=current.next
        return False

