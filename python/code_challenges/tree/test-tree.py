import pytest

from code_challenges.tree.tree import Tree, Node ,Binary_Tree


def test_empty_tree():
    tree = Binary_Tree()
    assert tree.root == None

def test_success_instantiate_tree_with_root_node():
    tree = Binary_Tree(88)
    assert tree.root == 88

def test_success_left_right_child():
    tree = Node(88)
    tree.left = Node(42)
    tree.right = Node(22)

    assert tree.left.value == 42
    assert tree.right.value == 22

def test_success_return_collection_pre_order(fixture_tree):
    result = fixture_tree.pre_order()
    assert result == [5, 4, 2, -1, 14, 16, 20]

def test_success_return_collection_post_order(fixture_tree):
    result = fixture_tree.post_order()
    assert result == [2, -1, 4, 16, 20, 14, 5]

def test_success_return_collection_in_order(fixture_tree):
    result = fixture_tree.in_order()
    assert result == [2, 4, -1, 5, 16, 14, 20]



