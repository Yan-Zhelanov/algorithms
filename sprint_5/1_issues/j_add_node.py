from node import Node

# Comment it before submitting
# class Node:
#     def __init__(self, left=None, right=None, value=0):
#         self.left = left
#         self.right = right
#         self.value = value


def insert(root, key):
    if key < root.value:
        if root.left is None:
            root.left = Node(None, None, key)
        else:
            insert(root.left, key)
    elif root.value <= key:
        if root.right is None:
            root.right = Node(None, None, key)
        else:
            insert(root.right, key)
    return root


def test_insert():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_insert()
