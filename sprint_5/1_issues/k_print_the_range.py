# Comment it before submitting
# class Node:
#     def __init__(self, left=None, right=None, value=0):
#         self.left = left
#         self.right = right
#         self.value = value


def print_range(node, left, right):
    if left <= node.value and node.left:
        print_range(node.left, left, right)
    if left <= node.value <= right:
        print(node.value, end=' ')
    if node.value <= right and node.right:
        print_range(node.right, left, right)


def test_print_range():
    node1 = Node(None, None, 2)
    node2 = Node(None, node1, 1)
    node3 = Node(None, None, 8)
    node4 = Node(None, node3, 8)
    node5 = Node(node4, None, 9)
    node6 = Node(node5, None, 10)
    node7 = Node(node2, node6, 5)
    print_range(node7, 2, 8)
    # expected output: 2 5 8 8


if __name__ == '__main__':
    test_print_range()
