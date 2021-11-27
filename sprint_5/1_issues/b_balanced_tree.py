# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right


def solution(root):
    tree = [root]
    index = 0
    depth = 0
    while depth >= 0:
        while (
            tree[index].left
            and getattr(tree[index].left, 'height', None) is None
        ):
            tree.append(tree[index].left)
            index = len(tree) - 1
            depth += 1
        if (
            tree[index].right
            and getattr(tree[index].right, 'height', None) is None
        ):
            tree.append(tree[index].right)
            index = len(tree) - 1
            depth += 1
            continue
        if getattr(tree[index], 'height', None) is None:
            tree[index].height = depth
        depth -= 1
        index -= 1
        tree.pop()
        if depth < 0:
            break
        if tree[index].left is None and tree[index].right is None:
            continue
        if tree[index].left is None:
            difference = abs(tree[index].right.height-depth)
        elif tree[index].right is None:
            difference = abs(tree[index].left.height-depth)
        elif (
            getattr(tree[index].left, 'height', None) is not None
            and getattr(tree[index].right, 'height', None) is not None
        ):
            difference = abs(tree[index].left.height-tree[index].right.height)
        else:
            continue
        if difference > 1:
            return False
        tree[index].height = max(
            getattr(tree[index].left, 'height', float('-inf')),
            getattr(tree[index].right, 'height', float('-inf')),
        )
    return True


def test_solution():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    result = solution(node5)
    assert result, 'Неверно! = ('
    node0 = Node(0)
    node1 = Node(1, node0, None)
    node2 = Node(-5, node1, None)
    node3 = Node(3, None, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    result = solution(node5)
    assert not result, 'Неверно! = ('
    node0 = Node(5)
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(2, None, node2)
    node4 = Node(3, node0, node1)
    node5 = Node(10, None, node3)
    node6 = Node(2, node4, node5)
    result = solution(node6)
    assert not result, 'Неверно! = ('
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_solution()
