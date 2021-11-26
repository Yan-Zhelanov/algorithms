# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def solution(root):
    def _is_balanced(root, depth):
        if root.left:
            left = _is_balanced(root.left, depth+1)
        if root.right:
            right = _is_balanced(root.right, depth+1)
        if left is False or right is False:
            return False
        if abs(left-right) > 1:
            return False
        return depth

    result = _is_balanced(root, 0)
    return False if result is False else True


def test_solution():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5), 'Неверно! = ('
    node0 = Node(0)
    node1 = Node(1, node0, None)
    node2 = Node(-5, node1, None)
    node3 = Node(3, None, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert not solution(node5), 'Неверно! = ('
    node0 = Node(5)
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(2, None, node2)
    node4 = Node(3, node0, node1)
    node5 = Node(10, None, node3)
    node6 = Node(2, node4, node5)
    assert not solution(node6), 'Неверно! = ('
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_solution()
