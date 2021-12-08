# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right


def solution(root):
    root.depth = 1
    tree = [root]
    index = 0
    max_depth = 0
    while index >= 0:
        while tree[index].left and tree[index].left not in tree:
            tree[index].left.depth = tree[index].depth + 1
            tree.append(tree[index].left)
            index = len(tree) - 1
        if tree[index].right and tree[index].right not in tree:
            tree[index].right.depth = tree[index].depth + 1
            tree.append(tree[index].right)
            index = len(tree) - 1
            continue
        if tree[index].depth > max_depth:
            max_depth = tree[index].depth
        index -= 1
    return max_depth


def test_solution():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)
    assert solution(node5) == 3
    assert solution(node3) == 2
    assert solution(node1) == 1
    node1 = Node(1, None, None)
    node2 = Node(4, None, node1)
    node3 = Node(3, node2, None)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)
    assert solution(node5) == 4
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_solution()
