# 55417030
class Deque:
    def __init__(self, max_size):
        self.deque = [0] * max_size
        self.max_size = max_size
        self.size = 0
        self.tail = 1
        self.head = 0

    def is_empty(self):
        return self.size == 0

    def is_max(self):
        return self.size == self.max_size

    def push_front(self, value):
        if self.is_max():
            raise IndexError('error')
        self.size += 1
        self.head = (self.head + 1) % self.max_size
        self.deque[self.head] = value

    def push_back(self, value):
        if self.is_max():
            raise IndexError('error')
        self.size += 1
        self.tail = (self.tail - 1) % self.max_size
        self.deque[self.tail] = value

    def pop_front(self):
        if self.is_empty():
            raise IndexError('error')
        self.size -= 1
        previous = self.head
        self.head = (self.head - 1) % self.max_size
        return self.deque[previous]

    def pop_back(self):
        if self.is_empty():
            raise IndexError('error')
        self.size -= 1
        previous = self.tail
        self.tail = (self.tail + 1) % self.max_size
        return self.deque[previous]


def run_commands(deque, commands):
    result = []
    for command in commands:
        if 'push_front' in command:
            try:
                deque.push_front(int(command.split()[1]))
            except IndexError as error:
                result.append(error)
        elif 'push_back' in command:
            try:
                deque.push_back(int(command.split()[1]))
            except IndexError as error:
                result.append(error)
        elif command == 'pop_front':
            try:
                result.append(deque.pop_front())
            except IndexError as error:
                result.append(error)
        else:
            try:
                result.append(deque.pop_back())
            except IndexError as error:
                result.append(error)
    return '\n'.join(str(line) for line in result)


def test_run_commands():
    deque = Deque(2)
    result = run_commands(deque, commands=[
        'push_front 10', 'push_front 30', 'pop_back', 'pop_front', 'pop_back',
        'push_back 1',
    ])
    assert result == '10\n30\nerror', f'Wrong answer: {result}'
    deque = Deque(4)
    result = run_commands(deque, commands=[
        'push_front 861', 'push_front -819', 'pop_back', 'pop_back',
    ])
    assert result == '861\n-819', f'Wrong answer: {result}'
    deque = Deque(10)
    result = run_commands(deque, commands=[
        'pop_back', 'pop_front', 'push_front -855', 'push_front 720',
        'pop_back', 'pop_back', 'push_back 844', 'pop_back', 'push_back 823',
    ])
    assert result == 'error\nerror\n-855\n720\n844', f'Wrong answer: {result}'
    deque = Deque(1)
    result = run_commands(deque, commands=[
        'push_back 1', 'push_front 2', 'push_back 3', 'push_front 4',
        'pop_back', 'pop_front', 'push_back -1', 'pop_front', 'pop_back',
        'pop_back',
    ])
    assert result == 'error\nerror\nerror\n1\nerror\n-1\nerror\nerror', (
        f'Wrong answer: {result}'
    )
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_run_commands()
    count = int(input())
    max_size = int(input())
    commands = [input() for _ in range(count)]
    print(run_commands(Deque(max_size), commands))
