
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
##########################66666##########################################


    def append(self,value):
        node1=Node(value)
        if not self.head:
            self.head=node1
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=node1

    def insert_before(self,value,new_value):

        new_node = Node(new_value)
        current = self.head
        if not self.head:
            self.head = new_node
        else:
            if current.value == value:
                th_node = self.head
                self.head = new_node
                new_node.next = th_node
                return
            else:
                    current = self.head
            while current.next :
                if current.next.value == value:
                    th_node = current.next
                    current.next = new_node
                    new_node.next = th_node
                    return
                else:
                    current = current.next
            return

    def insert_after(self, value, new_value):

        new_node = Node(new_value)
        current = self.head
        if not self.head:
                self.head = new_node
        else:
            current = self.head
            while current.next != None:
                if current.next.value == value:
                    current = current.next
                    old_node = current.next
                    current.next = new_node
                    new_node.next = old_node
                    return
                else:
                    current = current.next
            return
########################777777############################################
