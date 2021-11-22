# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left


def solution(root):
    depth = 0
    tree = [root]
    result = root.value
    while depth >= 0:
        while tree[depth].left and tree[depth].left not in tree:
            tree.append(tree[depth].left)
            depth = len(tree) - 1
            if tree[depth].value > result:
                result = tree[depth].value
        while tree[depth].right and tree[depth].right not in tree:
            tree.append(tree[depth].right)
            depth = len(tree) - 1
            if tree[depth].value > result:
                result = tree[depth].value
        depth -= 1
    return result


def test_solution():
    node_1 = Node(1)
    node_2 = Node(-5)
    node_3 = Node(3, node_1, node_2)
    node_4 = Node(2, node_3, None)
    result = solution(node_4)
    assert result == 3, f'Wrong answer: {result}'
    node_1 = Node(222)
    node_2 = Node(-5)
    node_3 = Node(3, node_1, node_2)
    node_4 = Node(2, node_3, None)
    result = solution(node_4)
    assert result == 222, f'Wrong answer: {result}'
    node_1 = Node(1)
    node_2 = Node(333)
    node_3 = Node(3, node_1, node_2)
    node_4 = Node(2, node_3, None)
    result = solution(node_4)
    assert result == 333, f'Wrong answer: {result}'
    node_1 = Node(-1)
    result = solution(node_1)
    assert result == -1, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_solution()
