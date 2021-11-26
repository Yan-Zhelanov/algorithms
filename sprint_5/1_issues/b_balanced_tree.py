# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def solution(root):
    tree = [root]
    depth = [0]
    current = 0
    current_depth = 0
    while current >= 0:
        while tree[current].left and tree[current].left not in tree:
            tree.append(tree[current].left)
            current = len(tree) - 1
            depth[current_depth] += 1
        depth.append(depth[current_depth])
        current_depth += 1
        while tree[current].right and tree[current].right not in tree:
            tree.append(tree[current].right)
            current = len(tree) - 1
            depth[current_depth] += 1
        if depth[current_depth] != depth[current_depth-1]:
            difference = abs(depth[current_depth]-depth[current_depth-1])
            if difference > 1:
                return False
        depth[current_depth] -= 1
        current -= 1
    return True


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
