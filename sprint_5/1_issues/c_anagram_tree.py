# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right


def bypass_tree(root, right=False):
    if root is None:
        return None, None
    tree = [root]
    if not right:
        left = [root.value]
        right = []
    else:
        left = []
        right = [root.value]
    depth = 0
    while depth >= 0:
        while tree[depth].left and tree[depth].left not in tree:
            tree.append(tree[depth].left)
            left.append(tree[depth].left.value)
            depth = len(tree) - 1
        if tree[depth].right and tree[depth].right not in tree:
            tree.append(tree[depth].right)
            right.append(tree[depth].right.value)
            depth = len(tree) - 1
            continue
        depth -= 1
    return left, right


def solution(root):
    left_1, right_1 = bypass_tree(root.left)
    left_2, right_2 = bypass_tree(root.right, True)
    return left_1 == right_2 and right_1 == left_2


def test_solution():
    node_1 = Node(3,  None,  None)
    node_2 = Node(4,  None,  None)
    node_3 = Node(4,  None,  None)
    node_4 = Node(3,  None,  None)
    node_5 = Node(2, node_1, node_2)
    node_6 = Node(2, node_3, node_4)
    node_7 = Node(1, node_5, node_6)
    assert solution(node_7)
    assert not solution(node_6)
    node_1 = Node(3,  None,  None)
    node_2 = Node(4,  node_1,  None)
    node_3 = Node(4,  None,  None)
    node_4 = Node(3,  node_2,  node_3)
    assert not solution(node_4)
    node_1 = Node(4,  None,  None)
    node_2 = Node(4,  None,  None)
    node_3 = Node(3,  node_1,  node_2)
    assert solution(node_3)
    node_1 = Node(4,  None,  None)
    assert solution(node_1)
    node_1 = Node(1,  None,  None)
    node_2 = Node(2,  None,  None)
    node_3 = Node(3,  node_2,  node_1)
    node_4 = Node(4,  None,  node_3)
    assert not solution(node_4)
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_solution()
