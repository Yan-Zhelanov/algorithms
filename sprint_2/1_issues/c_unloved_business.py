# class Node:
#     def __init__(self, value, next_item=None):
#         self.value = value
#         self.next_item = next_item


def get_node(head, index):
    while index > 0:
        head = head.next_item
        index -= 1
    return head


def solution(node, index):
    if index == 0:
        return node.next_item
    previous = get_node(node, index-1)
    previous.next_item = get_node(node, index+1)
    return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    while new_head:
        print(new_head.value, end=' -> ')
        new_head = new_head.next_item
    # result is node0 -> node2 -> node3


# if __name__ == '__main__':
#     test()
