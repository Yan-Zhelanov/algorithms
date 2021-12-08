# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left


def solution(root):
    numbers = []
    tree = [root]
    depth = 0
    current = f'{root.value}'
    changed = True
    while depth >= 0:
        while tree[depth].left and tree[depth].left not in tree:
            tree.append(tree[depth].left)
            depth = len(tree) - 1
            current += str(tree[depth].value)
            changed = True
        if tree[depth].right and tree[depth].right not in tree:
            tree.append(tree[depth].right)
            depth = len(tree) - 1
            current += str(tree[depth].value)
            changed = True
            continue
        if changed:
            changed = False
            numbers.append(int(current))
        number = str(tree[depth].value)
        if number == current[-len(number):]:
            current = current[:-len(number)]
        depth -= 1
    return sum(numbers)


def test_solution():
    node1 = Node(2, None, None)
    node2 = Node(1, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(2, None, None)
    node5 = Node(1, node4, node3)
    result = solution(node5)
    assert result == 275, f'Wrong answer: {result}'
    node1 = Node(200, None, None)
    node2 = Node(1, None, None)
    node3 = Node(3, node1, node2)
    result = solution(node3)
    assert result == 3231, f'Wrong answer: {result}'
    node1 = Node(3, None, None)
    node2 = Node(3, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(3, node3, None)
    node5 = Node(3, None, None)
    node6 = Node(3, node5, node4)
    result = solution(node6)
    assert result == 6699, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_solution()
