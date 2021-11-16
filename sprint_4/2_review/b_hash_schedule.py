class HashMap:
    MODULE = 6000011

    def __init__(self):
        self.items = [None] * self.MODULE

    def get_hash(self, key, ground=123):
        if key == '':
            return 0
        index = 0
        result = 0
        size = len(key) - 1
        module = self.MODULE
        while index < size:
            result = (((result + ord(key[index])) % module) * ground) % module
            index += 1
        return (result + ord(key[index])) % module

    def search(self, key):
        hashed_key = self.get_hash(key)
        while (
            self.items[hashed_key] is not None
            and self.items[hashed_key][0] != key
        ):
            hashed_key = (hashed_key + 2) % self.MODULE
        return hashed_key

    def put(self, key, value):
        self.items[self.search(key)] = (key, value)

    def get(self, key):
        item = self.items[self.search(key)]
        return 'None' if item is None else item[1]

    def delete(self, key):
        hashed_key = self.search(key)
        item = self.items[hashed_key]
        self.items[hashed_key] = None
        return 'None' if item is None else item[1]


def run_command(instance, name, key, value=None):
    command = getattr(instance, name)
    if value is None:
        return command(key)
    return command(key, value)


def run_commands(instance, commands):
    result = []
    for command in commands:
        command = command.split()
        if len(command) == 2:
            result.append(run_command(instance, command[0], command[1]))
            continue
        result.append(
            run_command(instance, command[0], command[1], command[2])
        )
    return '\n'.join(str(answer) for answer in result if answer is not None)


def test_run_commands():
    result = run_commands(HashMap(), [
        'get 1', 'put 1 10', 'put 2 4', 'get 1', 'get 2', 'delete 2', 'get 2',
        'put 1 5', 'get 1', 'delete 2',
    ])
    assert result == 'None\n10\n4\n4\nNone\n5\nNone', f'Wrong answer: {result}'
    result = run_commands(HashMap(), [
        'delete 2', 'get 1', 'put 34 4', 'get 1', 'delete 33', 'delete 34',
        'put 1 1', 'put 10000019 2', 'get 1', 'get 10000019'
    ])
    assert result == 'None\nNone\nNone\nNone\n4\n1\n2', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_run_commands()
    count = int(input())
    commands = [input() for _ in range(count)]
    print(run_commands(HashMap(), commands))
