
class Node:
    def __init__(self, value):
        self.value = value
        self.new_value = []

class K_ary_tree:
    def __init__(self):
        self.root = None



def tree_fizz_buzz(k_ary_tree):
    if not k_ary_tree.root:
        return "Tree is Empty"

    if tree.value % 3 == 0 and tree.value % 5 == 0:
            tree.value = 'FizzBuzz'
            values += [tree.value]
    elif tree.value % 3 == 0:
            tree.value = 'Fizz'
            values += [tree.value]
    elif tree.value % 5 == 0:
            tree.value = 'Buzz'
            values += [tree.value]
    else:
            values += [str(tree.value)]

   

    return values
