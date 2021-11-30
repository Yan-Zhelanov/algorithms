# Comment it before submitting
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.left = left
        self.right = right
        self.value = value


def search(root, key):
    if root.value == key:
        return None, root
    tree = [root]
    index = 0
    while index >= 0:
        while tree[index].left and not getattr(tree[index].left, 'checked', False):
            tree.append(tree[index].left)
            index = len(tree) - 1
            tree[index].checked = True
        if tree[index].right and not getattr(tree[index].right, 'checked', False):
            tree.append(tree[index].right)
            index = len(tree) - 1
            tree[index].checked = True
            continue
        if tree[index].value == key:
            return tree[index-1], tree[index]
        index -= 1
        tree.pop()
    return None, None


def remove(root, key):
    parent, target = search(root, key)
    if target is None:
        return root
    if parent is None:
        pass
    return root


def test_remove():
    node_1 = Node(None, None, 2)
    node_2 = Node(node_1, None, 3)
    node_3 = Node(None, node_2, 1)
    node_4 = Node(None, None, 6)
    node_5 = Node(node_4, None, 8)
    node_6 = Node(node_5, None, 10)
    node_7 = Node(node_3, node_6, 5)
    new_head = remove(node_7, 10)
    assert new_head.value == 5, f'Wrong answer: {new_head.value}'
    assert new_head.right is node_5, f'Wrong answer: {new_head.right}'
    assert new_head.right.value == 8, f'Wrong answer: {new_head.right.value}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_remove()
