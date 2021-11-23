# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left


def solution(root):
    def _check_previous(operations, current):
        index = len(operations) - 1
        while index >= 0:
            if (
                operations[index][1] == 'less'
                and not current < operations[index][0]
            ):
                return False
            elif (
                operations[index][1] == 'more'
                and not operations[index][0] < current
            ):
                return False
            index -= 1
        return True

    depth = 0
    tree = [root]
    operations = []
    while depth >= 0:
        while tree[depth].left and tree[depth].left not in tree:
            if (
                not tree[depth].left.value < tree[depth].value
                or operations
                and not _check_previous(operations, tree[depth].left.value)
            ):
                return False
            tree.append(tree[depth].left)
            operations.append([tree[depth].value, 'less'])
            depth = len(tree) - 1
        while tree[depth].right and tree[depth].right not in tree:
            if (
                not tree[depth].value < tree[depth].right.value
                or operations
                and not _check_previous(operations, tree[depth].right.value)
            ):
                return False
            tree.append(tree[depth].right)
            operations.append([tree[depth].value, 'more'])
            depth = len(tree) - 1
        if operations:
            operations.pop()
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
