class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1]


class StackMaxEffective:
    def __init__(self):
        self.stack = []
        self.max = Stack()

    def push(self, value):
        self.stack.append(value)
        max_value = self.get_max()
        max_value = float('-inf') if max_value is None else max_value
        if value >= max_value:
            self.max.push(value)

    def pop(self):
        try:
            saved = self.stack.pop()
        except IndexError:
            raise IndexError('error')
        if saved == self.get_max():
            self.max.pop()

    def get_max(self):
        try:
            return self.max.top()
        except IndexError:
            return None


def run_commands(stack, commands):
    result = []
    for command in commands:
        if 'push' in command:
            stack.push(int(command.split()[1]))
        elif command == 'pop':
            try:
                stack.pop()
            except IndexError as error:
                result.append(error)
        else:
            result.append(stack.get_max())
    return '\n'.join(str(line) for line in result)


def test_run_commands():
    stack = StackMaxEffective()
    result = run_commands(stack, commands=[
        'get_max', 'push 7', 'pop', 'push -2', 'push -1', 'pop', 'get_max',
        'get_max',
    ])
    assert result == 'None\n-2\n-2', f'Wrong answer: {result}'
    stack = StackMaxEffective()
    result = run_commands(stack, commands=[
        'get_max', 'pop', 'pop', 'push 10', 'get_max', 'push -9', 'push 333',
        'get_max', 'pop', 'pop', 'pop', 'pop', 'get_max',
    ])
    assert result == 'None\nerror\nerror\n10\n333\nerror\nNone', (
        f'Wrong answer: {result}'
    )
    stack = StackMaxEffective()
    result = run_commands(stack, commands=[
        'push -10', 'get_max', 'push -12', 'get_max', 'push -9', 'get_max',
        'push -9', 'pop', 'get_max', 'push -8', 'push 8', 'get_max', 'pop',
        'get_max', 'push -8', 'get_max', 'push 8', 'push 8', 'push 8',
        'push -8', 'get_max', 'pop', 'pop', 'pop', 'pop', 'pop', 'pop', 'pop',
        'pop', 'pop', 'pop', 'pop', 'pop', 'pop', 'get_max', 'get_max',
        'get_max', 'push 8', 'get_max', 'push 0', 'push 0', 'get_max',
        'push 8', 'get_max', 'get_max', 'pop', 'get_max', 'push 8', 'push 0',
        'get_max', 'pop', 'get_max', 'pop', 'get_max', 'pop', 'get_max'
    ])
    assert result == (
        '-10\n-10\n-9\n-9\n8\n-8\n-8\n8\nerror\nerror\nerror\nerror\nNone'
        '\nNone\nNone\n8\n8\n8\n8\n8\n8\n8\n8\n8'
    ), f'Wrong answer: {result}'
    stack = StackMaxEffective()
    result = run_commands(stack, commands=[
        'push 0', 'push -5', 'get_max',
    ])
    assert result == '0', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_run_commands()
    count = int(input())
    commands = [input() for _ in range(count)]
    print(run_commands(StackMaxEffective(), commands))
