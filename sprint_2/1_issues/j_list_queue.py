class Node:
    def __init__(self, value, previous=None, next_node=None):
        self.value = value
        self.next_node = next_node


class Queue:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get(self):
        if self.is_empty():
            raise IndexError('error')
        self.size -= 1
        saved = self.head
        self.head = self.head.next_node
        return saved.value

    def put(self, value):
        tail = Node(value)
        if self.size == 0:
            self.head = tail
        else:
            self.tail.next_node = tail
        self.tail = tail
        self.size += 1

    def get_size(self):
        return self.size


def run_commands(queue, commands):
    result = []
    for command in commands:
        if 'put' in command:
            queue.put(int(command.split()[1]))
        elif command == 'get':
            try:
                result.append(queue.get())
            except IndexError as error:
                result.append(error)
        else:
            result.append(queue.get_size())
    return '\n'.join(str(line) for line in result)


def test_run_commands():
    queue = Queue()
    result = run_commands(queue, commands=[
        'put -34', 'put -23', 'get', 'size', 'get', 'size', 'get', 'get',
        'put 80', 'size',
    ])
    assert result == '-34\n1\n-23\n0\nerror\nerror\n1', f'Wrong answer: {result}'
    queue = Queue()
    result = run_commands(queue, commands=[
        'size', 'put 0', 'size', 'get', 'get', 'size', 'put 1', 'put 2',
        'put 3', 'put 4', 'put 5', 'size',
    ])
    assert result == '0\n1\n0\nerror\n0\n5', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_run_commands()
    count = int(input())
    commands = [input() for _ in range(count)]
    print(run_commands(Queue(), commands))
