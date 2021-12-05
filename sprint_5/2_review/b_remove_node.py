# 60036741

"""
    --- Принцип работы ---
Для начала сделаем наш массив кучей, для этого будем искать самые большие
элементы с середины массива, потому что веток у других элементов нет, так как,
если умножить их индекс на двойку, то мы выйдем за размер массива. Далее будем
для нулевого индекса искать самый большой элемент в массиве, после будем
менять его местами с последним неотсортированным местом в массиве, запускать
повторно поиск самого большого элемента, не проверяя при этом последние
отсортированные элементы.

    --- Доказательство корректности ---
Из описания следует, что мы будем находить самый большой элемент в массиве, а
после ставить его в конец, эта операция будет повторяться, пока площадь поиска
не будет равна единице, тогда на нулевом элементе останется один элемент, его
сортировать не нужно, он уже самый маленький.

    --- Временная сложность ---
В худшем, среднем и лучшем случаях: O(n * log(n))

    --- Пространственная сложность ---
Реализация требует хранить три индекса, в худшем случае, когда поиск самого
большого элемента запущен с нулевого индекса и каждый раз будет происходить
перестановка, то-есть нахождение большего элемента, то в худшем случае, глубина
вызов будет log(n), таким образом в худшем случае: O(log(n) * 3) = O(log(n))
В лучшем случае: O(1)
В среднем случае: O(log(n))
"""

# Comment it before submitting
# class Node:
#     def __init__(self, left=None, right=None, value=0):
#         self.left = left
#         self.right = right
#         self.value = value


def search(root, key):
    if root.value == key:
        return None, root
    parent = root
    while root.left or root.right:
        if root.value > key and root.left:
            parent = root
            root = root.left
        elif root.value < key and root.right:
            parent = root
            root = root.right
        else:
            break
    if root.value == key:
        return parent, root
    return None, None


def get_replacement(root):
    if root.left:
        child = root.left
        if not child.right:
            root.left = child.left
        else:
            while child.right:
                root = child
                child = child.right
            root.right = child.left
        child.left = None
        return child
    if root.right:
        child = root.right
        if not child.left:
            root.right = child.right
        else:
            while child.left:
                root = child
                child = child.left
            root.left = child.right
        child.right = None
        return child
    return None


def remove(root, key):
    if root is None:
        return None
    parent, target = search(root, key)
    if target is None:
        return root
    replacement = get_replacement(target)
    if replacement is None:
        if parent is None:
            return None
        if parent.left is target:
            parent.left = None
            return root
        parent.right = None
        return root
    if parent is None:
        replacement.left = target.left
        replacement.right = target.right
        return replacement
    if parent.left is target:
        parent.left = replacement
    else:
        parent.right = replacement
    replacement.left = target.left
    replacement.right = target.right
    return root


def test_remove():
    node_1 = Node(None, None, 1)
    node_2 = Node(None, None, 3)
    node_3 = Node(None, None, 4)
    node_4 = Node(None, None, 12)
    node_5 = Node(node_1, node_2, 2)
    node_6 = Node(node_3, None, 5)
    node_7 = Node(None, None, 7)
    node_8 = Node(None, node_4, 10)
    node_9 = Node(node_5, node_6, 3)
    node_10 = Node(node_7, node_8, 8)
    node_11 = Node(node_9, node_10, 5)
    new_head = remove(node_11, 3)
    assert new_head.value == 5
    assert new_head is node_11
    assert new_head.right.value == 8
    assert new_head.left.value == 3
    assert new_head.left.left.right is None
    new_head = remove(new_head, 3)
    assert new_head.value == 5
    assert new_head.left.value == 2
    assert new_head.left.left.value == 1
    assert new_head.left.right.value == 5
    node_1 = Node(None, None, 2)
    node_2 = Node(node_1, None, 3)
    node_3 = Node(None, node_2, 1)
    node_4 = Node(None, None, 6)
    node_5 = Node(node_4, None, 8)
    node_6 = Node(node_5, None, 10)
    node_7 = Node(node_3, node_6, 5)
    new_head = remove(node_7, 1)
    assert new_head.value == 5
    assert new_head.left is node_1
    assert new_head.left.value == 2
    new_head = remove(new_head, 6)
    assert new_head.value == 5
    assert new_head.right is node_6
    assert new_head.right.value == 10
    assert new_head.right.left.left is None
    new_head = remove(new_head, 10)
    assert new_head.value == 5
    assert new_head.right is node_5
    assert new_head.right.value == 8
    new_head = remove(new_head, 5)
    assert new_head.value == 3
    assert new_head.value < new_head.right.value
    assert new_head is node_2
    assert new_head.left.value == 2
    assert new_head.right.value == 8
    new_head = remove(new_head, 5)
    assert new_head.value == 3
    assert new_head.value < new_head.right.value
    assert new_head is node_2
    assert new_head.left.value == 2
    assert new_head.right.value == 8
    new_head = remove(new_head, 3)
    assert new_head.value == 2
    assert new_head is node_1
    assert new_head.right.value == 8
    new_head = remove(new_head, 2)
    assert new_head.value == 8
    new_head = remove(new_head, 8)
    assert new_head is None
    new_head = remove(None, 5)
    assert new_head is None
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_remove()
