class Queue:
    def __init__(self, max_size):
        self.queue = [0] * max_size
        self.max_size = max_size
        self.size = 0
        self.tail = 0
        self.head = 0

    def is_empty(self):
        return self.size == 0

    def is_max(self):
        return self.size == self.max_size

    def push(self, value):
        if self.is_max():
            raise IndexError('error')
        self.size += 1
        self.queue[self.head] = value
        self.head = (self.head + 1) % self.max_size

    def pop(self):
        if self.is_empty():
            return None
        self.size -= 1
        previous = self.tail
        self.tail = (self.tail + 1) % self.max_size
        return self.queue[previous]

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.tail]

    def get_size(self):
        return self.size


def run_commands(queue, commands):
    result = []
    for command in commands:
        if 'push' in command:
            try:
                queue.push(int(command.split()[1]))
            except IndexError as error:
                result.append(error)
        elif command == 'pop':
            result.append(queue.pop())
        elif command == 'peek':
            result.append(queue.peek())
        else:
            result.append(queue.get_size())
    return '\n'.join(str(line) for line in result)


def test_run_commands():
    queue = Queue(2)
    result = run_commands(queue, commands=[
        'push 7', 'peek', 'pop', 'pop', 'push 10', 'push -13', 'peek', 'pop',
        'peek',
    ])
    assert result == '7\n7\nerror\n10\n10\n-13', f'Wrong answer: {result}'
    queue = Queue(2)
    result = run_commands(queue, commands=[
        'peek', 'push 5', 'push 2', 'peek', 'size', 'size', 'push 1', 'size'
    ])
    assert result == 'None\n5\n2\n2\nerror\n2', f'Wrong answer: {result}'
    queue = Queue(1)
    result = run_commands(queue, commands=[
        'push 3', 'peek', 'size', 'pop', 'pop', 'push 3', 'push 4'
    ])
    assert result == '3\n1\n3\nerror\nerror', f'Wrong answer: {result}'
    queue = Queue(1)
    result = run_commands(queue, commands=[
        'push 1', 'size', 'push 3', 'size', 'push 1', 'pop', 'push 1', 'pop',
        'push 3', 'push 3',
    ])
    assert result == '1\nerror\n1\nerror\n1\n1\nerror', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_run_commands()
    count = int(input())
    max_size = int(input())
    commands = [input() for _ in range(count)]
    print(run_commands(Queue(max_size), commands))
