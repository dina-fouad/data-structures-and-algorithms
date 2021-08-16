

class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None


class Binary_Tree:

    def __init__(self, root = None):
        self.root = root

    def pre_order(self):

        pre_out = []
        def pre(root):
            pre_out.append(root.value)

            if root.left:
                pre(root.left)

            if root.right:
                pre(root.right)

        pre(self.root)

        return pre_out

    def in_order(self):


        in_out = []
        def walk(root):

            if root.left:
                walk(root.left)
            in_out.append(root.value)

            if root.right:
                walk(root.right)


class Binary_Search_Tree(Binary_Tree):


    def add(self, value):

        if not self.root:
            self.root = Node(value)
        else:
            def walk(roots):
                if value < roots.value:
                    if not roots.left:
                        roots.left = Node(value)
                        return
                    else:
                        walk(roots.left)
                else:
                    if not roots.right:
                        roots.right = Node(value)
                        return
                    else:
                        walk(roots.right)
            walk(self.root)

    def contains(self, value):

        if not self.root:
            return False
        current = self.root
        while True:
            if value == current.value:
                return True
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    return False
            else:
                if current.right:
                    current = current.right
                else:
                    return False

                    #####code challenge 16 ###########


    def find_tree_max_number(self):
        max_number =0
        if not self.root.value :
            return " empty Tree"

        else:
            list = self.in_order()
            for n in list :
                if n > max_number:
                    max_number= n
        return max_number
