class StackMax:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        try:
            self.stack.pop()
        except IndexError:
            raise IndexError('error')

    def get_max(self):
        try:
            return max(self.stack)
        except ValueError:
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
    stack = StackMax()
    result = run_commands(stack, commands=[
        'get_max', 'push 7', 'pop', 'push -2', 'push -1', 'pop', 'get_max',
        'get_max',
    ])
    assert result == 'None\n-2\n-2', f'Wrong answer: {result}'
    stack = StackMax()
    result = run_commands(stack, commands=[
        'get_max', 'pop', 'pop', 'push 10', 'get max', 'push -9', 'push 333',
        'get_max', 'pop', 'pop', 'pop', 'pop', 'get_max',
    ])
    assert result == 'None\nerror\nerror\n10\n333\nerror\nNone', (
        f'Wrong answer: {result}'
    )
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_run_commands()
    count = int(input())
    commands = [input() for _ in range(count)]
    print(run_commands(StackMax(), commands))
