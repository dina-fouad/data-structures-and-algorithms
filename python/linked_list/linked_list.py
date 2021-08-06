
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
