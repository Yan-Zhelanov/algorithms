# class Node:
#     def __init__(self, value, next_item=None):
#         self.value = value
#         self.next_item = next_item


def solution(node, elem):
    index = 0
    while node.value != elem:
        node = node.next_item
        if not node:
            return -1
        index += 1
    return index


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    index = solution(node0, "node2")
    assert index == 2, f'Wrong answer: {index}'
    index = solution(node0, "node5")
    assert index == -1, f'Wrong answer: {index}'
    index = solution(node0, "node0")
    assert index == 0, f'Wrong answer: {index}'
    index = solution(node0, "node3")
    assert index == 3, f'Wrong answer: {index}'


# if __name__ == '__main__':
#     test()
