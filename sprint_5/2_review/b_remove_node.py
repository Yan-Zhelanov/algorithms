# Comment it before submitting
# class Node:
#     def __init__(self, left=None, right=None, value=0):
#         self.left = left
#         self.right = right
#         self.value = value


def remove(root, key):
    def _search(root, key):
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

    def _get_replacement(root):
        if root.left:
            child = root.left
            while child.right:
                root = child
                child = child.right
            root.right = None
            if child.left:
                root.right = child.left
            return child
        if root.right:
            child = root.right
            while child.left:
                root = child
                child = child.left
            root.left = None
            if child.right:
                root.left = child.right
            return child
        return None

    parent, target = _search(root, key)
    if target is None:
        if parent.right is target:
            parent.right = None
        else:
            parent.left = None
        return root
    replacement = _get_replacement(target)
    if replacement is None:
        if parent.left is target:
            parent.left = None
        else:
            parent.right = None
        return root
    if parent is None:
        replacement.left = target.left
        replacement.right = target.right
        return replacement
    if parent.left is target:
        parent.left = replacement
        replacement.left = target.left
        replacement.right = target.right
        return root
    parent.right = replacement
    replacement.left = target.left
    replacement.right = target.right
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
    new_head = remove(new_head, 5)
    assert new_head.value == 3, f'Wrong answer: {new_head.value}'
    assert new_head.left is node_3, f'Wrong answer: {new_head.left}'
    assert new_head.left.value == 1, f'Wrong answer: {new_head.left.value}'
    assert new_head.left.right is node_1, f'Wrong answer: {new_head.left.right}'
    assert new_head.left.right.value == 2, f'Wrong answer: {new_head.left.right.value}'
    node_1 = Node(None, None, 2)
    node_2 = Node(node_1, None, 3)
    node_3 = Node(None, node_2, 1)
    node_4 = Node(None, None, 6)
    node_5 = Node(node_4, None, 8)
    node_6 = Node(node_5, None, 10)
    node_7 = Node(node_3, node_6, 5)
    new_head = remove(node_7, 1)
    assert new_head.value == 5, f'Wrong answer: {new_head.value}'
    assert new_head.left is node_1, f'Wrong answer: {new_head.left}'
    assert new_head.left.value == 2, f'Wrong answer: {new_head.left.value}'
    new_head = remove(new_head, 6)
    assert new_head.value == 5, f'Wrong answer: {new_head.value}'
    assert new_head.right is node_6, f'Wrong answer: {new_head.right}'
    assert new_head.right.value == 10, f'Wrong answer: {new_head.right.value}'
    assert new_head.right.left.left is None, f'Wrong answer: {new_head.right.left.left}'
    print('Все тесты пройдены!')


# if __name__ == '__main__':
#     test_remove()
