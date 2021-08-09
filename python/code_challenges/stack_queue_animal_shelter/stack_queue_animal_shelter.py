class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class EmptyQueueException(Exception):
    pass
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,value):
        new_node= Node(value)
        if not self.front:
            self.front= new_node
            self.rear= new_node
        else:
            self.rear.next=new_node
            self.rear= new_node

    def __str__(self):
        current=self.front
        items= []
        while current:
            items.append(str(current.value))
            current=current.next
        return f" <- ".join(items)

    def IsEmpty(self):
        return self.front == None
    def dequeue (self):
        if not self.front :
            raise EmptyQueueException()
        else:
            temp = self.front
            self.front=self.front.next
            temp.next= None
            return temp.value




class Cat():
    def __init__(self, name):
        self.name = name
        self.type = "cat"


class Dog():
    def __init__(self, name):
        self.name = name
        self.type = "dog"



class AnimalShelter :
    def __init__(self,):
        self.cat=Queue()
        self.dog = Queue()

    def enqueue(self,animal) :
        if animal.type== 'dog':
            self.dog.enqueue(animal.name)
        if animal.type== 'cat':
            self.cat.enqueue(animal.name)
        else : return "Null"

    def dequeue(self, pref):
        if pref == "cat":
            self.cat.dequeue()
        elif pref == "dog":
            self.dog.dequeue()
        else:
            return "Null"
