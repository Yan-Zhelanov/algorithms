# 60036741

"""
    --- Принцип работы ---
Воспользуемся свойствами бинарного дерева поиска и найдём по ключу элемент,
который нужно удалить, и его родителя. Если элемент — это корень дерева, то
родителя не существует, значит нужно найти элемент на замену и присвоить левому
и правому ребёнку детей удаляемой вершины. Если элемент найден и у него есть
родитель, значит нужно удалить ссылку из родителя на этот элемент и назначить
новый, которым делаем замену, остальное так же, как и в первом варианте. Если
элемент не найден возвращаем корень дерева.
Поиск элемента на замену происходит следующим образом: если у удаляемого дерева
есть левое поддерево, то искать будем в нём, если левого нет, то искать будем
в правом поддереве, если ни левого ни правого поддерева нет, значит наш элемент
— это лист, достаточно просто удалить ссылку из родителя на этот элемент.
Искать в левом поддереве будем самый правый элемент, а в правом поддереве самый
левый, так как эти числа будут максимально близки к удаляемому числу и не
сломают свойства нашего бинарного дерева поиска. Родителю заменяемого элемента
обязательно нужно "отдать" ребёнка заменяемого элемента на место заменяемого,
иначе он останется висеть в воздухе.

    --- Доказательство корректности ---
Из описания следует, что если подаваемое на вход дерево является бинарным
деревом поиска, то алгоритм верно найдёт удаляемый элемент и элемент на его
замену, а значит дерево не распадётся и все его свойства будут сохранены.

    --- Временная сложность ---
Для поиска элемента в худшем случае мы сделаем H операций, где H — это высота
дерева, для нахождения элемента на замену в худшем случае мы выполним H-1
операций, но в таком случае поиск удаляемого элемента у нас займёт 1 операцию,
а если поиск удаляемого элемента занял H операций, то удаляемый элемент — лист,
а это значит, что искать заменяемый элемент не придётся. В общем, на поиск
удаляемого элемента и поиск замены мы потратим H операций. Остальные операции
выполняются константное время, значит итоговая сложность: O(H)

    --- Пространственная сложность ---
В худшем и среднем случае требуется хранить 3 указателя на удаляемый элемент,
на его родителя и на заменяемый элемент, в лучшем случае, если искомый элемент
не найден, то дополнительная память вообще не требуется.
Итого: O(1)
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
