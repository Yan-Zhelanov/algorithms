# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root):
    depth = 0
    tree = [root]
    while depth >= 0:
        while tree[depth].left and tree[depth].left not in tree:
            index = depth
            left = tree[depth].left.value
            # в таком случае если дерево 1 -> 5 -> 3, то 3 будет больше 1
            while index >= 0:
                if not left < tree[index].value:
                    return False
                index -= 1
            tree.append(tree[depth].left)
            depth = len(tree) - 1
        while tree[depth].right and tree[depth].right not in tree:
            if not tree[depth].value < tree[depth].right.value:
                return False
            tree.append(tree[depth].right)
            depth = len(tree) - 1
        depth -= 1
    return True


def test_solution():
    node_1 = Node(1, None, None)
    node_2 = Node(4, None, None)
    node_3 = Node(3, node_1, node_2)
    node_4 = Node(8, None, None)
    node_5 = Node(5, node_3, node_4)
    assert solution(node_5)
    node_2.value = 5
    assert not solution(node_5)
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_solution()
