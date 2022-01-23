class Node:
    def __init__(self, value, next=None):
        self.terminal = False
        self.value = value
        self.next = {} if next is None else next


def add_string(root, string, index):
    current_node = root
    for i in range(len(string)):
        symbol = string[i]
        if not current_node.next.get(symbol, False):
            new_node = Node(symbol)
            current_node.next[symbol] = new_node
        current_node = current_node.next[symbol]
    current_node.terminal = index
    return current_node


def build_trie(strings):
    root = Node('')
    for index, string in enumerate(strings):
        add_string(root, string, index)
    return root


def search_patterns_in_string(root_patterns, string):
    current_node = root_patterns
    for position in range(len(string)):
        symbol = string[position]
        if symbol.islower():
            continue
        if current_node.next.get(symbol, False):
            current_node = current_node.next[symbol]
            if current_node.terminal is not False:
                return current_node.terminal
    return -1


def global_search(strings, patterns):
    root = build_trie(patterns)
    finded = [[] for _ in range(len(patterns))]
    for string in strings:
        index = search_patterns_in_string(root, string)
        if index != -1:
            finded[index].append(string)
    finded = [sorted(strings) for strings in finded]
    return '\n'.join(string for strings in finded for string in strings)


def test_search():
    result = global_search(
        [
            'MamaMilaRamu',
            'MamaMia',
            'MonAmi',
        ],
        [
            'MM',
            'MA',
        ]
    )
    assert result == 'MamaMia\nMamaMilaRamu\nMonAmi', f'Wrong answer: {result}'
    result = global_search(
        [
            'KekK',
            'LeKkkk',
            'ShreKK',
        ],
        [
            'KKK',
            'LK',
        ]
    )
    assert result == 'LeKkkk', f'Wrong answer: {result}'
    result = global_search(
        [
            'KekK',
            'LeKkkk',
            'ShreKK',
        ],
        [
            'WGTRK',
        ]
    )
    assert result == '', f'Wrong answer: {result}'
    result = global_search(
        [
            'CheBuReK',
        ],
        [
            '',
            'CBRK',
        ]
    )
    assert result == 'CheBuReK', f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    test_search()
    strings = [input() for _ in range(int(input()))]
    patterns = [input() for _ in range(int(input()))]
    print(global_search(strings, patterns))
