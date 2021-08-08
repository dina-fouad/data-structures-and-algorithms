
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


    def kth_from_end(self, k):
        current = self.head
        arr = []
        if k < 0:
            return 'index can\'t be less the zero'
        while current:
            arr.append(current)
            current = current.next
        if len(arr) < k:
            return 'index not found'
        arr.reverse()
        if k == len(arr):
            k = k -1
        return arr[k].value

########################88888############################################


def ziplist(ll1, ll2):

    new_ll=LinkedList()
    max_len=max(ll1.length,ll2.length)
    ll1_curent=ll1.head
    ll2_curent=ll2.head
    if ll1.length or ll2.length:
        for i in range(max_len):
            if ll1_curent:
                new_ll.append(ll1_curent.value)
                ll1_curent=ll1_curent.next
            if ll2_curent:
                new_ll.append(ll2_curent.value)
                ll2_curent=ll2_curent.next
        print(new_ll.to_string())
        return new_ll
    else:
        return "Sorry invalid input"
