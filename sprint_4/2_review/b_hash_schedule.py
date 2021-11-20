# 58743014

"""
    --- Принцип работы ---
За основу возьмём массив, пустые ячейки будем отмечать, как None, удалённые
ячейки будем отмечать как 'deleted' в остальных ячейках будем хранить кортежи,
где на первом месте будет лежать ключ, на втором значение. Так как мы заранее
знаем количество запросов, подберём оптимальный модуль, длинна массива будет
равна этому модулю. Для разрешения коллизий будем использовать метод линейной
открытой адресации, поэтому для поиска по ключу будем хешировать ключ и
двигаться по массиву, пока не встретим None или, если мы используем поиск для
вставки, пока не встретим удалённую ячейку, то-есть такого ключа ещё нет в
массиве, иначе пока не встретим кортеж, с точно таким же ключём на первом
месте. Поиск по ключу это основная операция, на которой будут основываться все
остальные действия: добавление, получение и удаление. Для добавления элемента
или его перезаписи достаточно запустить поиск и перезаписать ячейку. Тоже самое
с получением, только перезаписывать ячейку мы не будем, а если в ячейке лежит
None, то-есть такого ключа ещё не было добавленно в хеш-таблицу, как и
требуется в задании мы будем возвращать строку с None. Удаление работает,
как эти два метода объединённые вместе, только перезаписывать ячейку мы всегда
будем как удалённую, чтобы облегчить поиски в будущем. В случае, если кортежа в
ячейке не было, вернём None.

    --- Доказательство корректности ---
Из описания следует, что все операции основываются на поиске, поэтому если
поиск работает верно, то и добавление, получение и удаление работают верно.
Модуль, то-есть размер массива у нас не меняется, он всегда простое нечётное
число, поэтому для того, чтобы разрешать коллизии я выбрал двойку. Ведь даже
если все элементы будут захешированны одним ключём, поиск пройдётся по каждой
ячейке массива, пока не пройдёт каждую или не найдёт пустую, так как у двойки и
простого нечётного числа нет общих делителей, то поиск обязательно проверит
каждый элемент массива. Таким образом поиск всегда будет возвращать, либо
ячейку с нужным ключём, либо пустую ячейку, либо удалённую в случае поиска для
вставки. Если поиск пройдётся по всему массиву, но не найдёт нужной ячейки,
поиск вернёт None, в случае, если поиск выполнялся для вставки, программа
предупредит, что было переполнение.

    --- Временная сложность ---
Поиск в худшем случае, когда все элементы будут захешированны одним значением,
будет занимать: O(n), где n — длинна массива, в лучшем и среднем случае поиск
будет работать за O(1).
Так как все остальные операции зависят от поиска, их сложность будет равна
сложности поиска.

    --- Пространственная сложность ---
В лучшем случае мы будем хранить массив с константным количеством None, где
количество зависит от модуля: O(n) — где n, это модуль. В среднем и худшем
случае мы будем хранить n кортежей с ключами и значениями элементов:
O(n*2) = O(n)
"""


class HashMap:
    MODULE = 1000003
    DELETED = 'deleted'

    def __init__(self):
        self.items = [None] * self.MODULE

    def get_hash(self, key, ground=113):
        if key == '':
            return 0
        index = 0
        result = 0
        size = len(key) - 1
        module = self.MODULE
        while index < size:
            result = ((result + int(key[index]) % module) * ground) % module
            index += 1
        return (result + int(key[index])) % module

    def search(self, key, put=False):
        hashed_key = self.get_hash(key)
        index = 0
        item = self.items[hashed_key]
        while not (
            item is None or put and item == self.DELETED
            or item != self.DELETED and item[0] == key
        ) and index < self.MODULE:
            hashed_key = (hashed_key + 2) % self.MODULE
            item = self.items[hashed_key]
            index += 1
        return hashed_key if index < self.MODULE else None

    def put(self, key, value):
        hashed_key = self.search(key, True)
        if hashed_key is None:
            raise IndexError('Overflow')
        self.items[hashed_key] = (key, value)

    def get(self, key):
        hashed_key = self.search(key)
        if hashed_key is None:
            return None
        item = self.items[hashed_key]
        return None if item is None else item[1]

    def delete(self, key):
        hashed_key = self.search(key)
        if hashed_key is None:
            return None
        item = self.items[hashed_key]
        if item is None:
            return None
        self.items[hashed_key] = self.DELETED
        return item[1]


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
        try:
            run_command(instance, command[0], command[1], command[2])
        except IndexError as error:
            result.append(error)
    return '\n'.join(str(answer) for answer in result)


def test_run_commands():
    result = run_commands(HashMap(), [
        'get 1', 'put 1 10', 'put 2 4', 'get 1', 'get 2', 'delete 2', 'get 2',
        'put 1 5', 'get 1', 'delete 2',
    ])
    assert result == 'None\n10\n4\n4\nNone\n5\nNone', f'Wrong answer: {result}'
    result = run_commands(HashMap(), [
        'delete 2', 'get 1', 'put 34 4', 'get 1', 'delete 33', 'delete 34',
        'put 1 1', 'put 1000003 2', 'get 1', 'get 1000003'
    ])
    assert result == 'None\nNone\nNone\nNone\n4\n1\n2', (
        f'Wrong answer: {result}'
    )
    result = run_commands(HashMap(), [
        'put 1 1', 'put 2 2', 'put 3 3', 'delete 2', 'get 3', 'get 1', 'get 2'
    ])
    assert result == '2\n3\n1\nNone', (
        f'Wrong answer: {result}'
    )
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_run_commands()
    result = []
    count = int(input())
    hash_map = HashMap()
    for _ in range(count):
        command = input().split()
        if len(command) == 2:
            result.append(run_command(hash_map, command[0], command[1]))
            continue
        try:
            run_command(hash_map, command[0], command[1], command[2])
        except IndexError as error:
            result.append(error)
    print('\n'.join(str(answer) for answer in result))
