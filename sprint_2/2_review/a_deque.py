# 55472703

"""
    --- Принцип работы ---
Для реализации я использовал обычный массив, так как максимальная длинна
заранее известна, я сразу же зарезервировал в памяти место для каждой ячейки.
Переменная size при добавлении в хвост или голову увеличивается на единицу,
это сделанно для того, чтобы знать, когда массив переполнен и поднять
исключение с ошибкой. А так же, чтобы знать, когда массив пуст и из него
просто нечего доставать, чтобы так же поднять исключение.
Переменная tail выставленна на единицу, чтобы при добавлении в хвост или
голову, когда в массиве только один элемент, оба указателя (tail, head)
хранили индекс единственного элемента для его получения в дальнейшем.
При самом добавлении в хвост индекс tail уменьшается, так как элемент должен
быть позади остальных, при добавлении в голову индекс head наоборот
увеличивается, чтобы добавить элемент в самую "переднюю" ячейку.
При удалении индекс головы наоборот уменьшается, а хвоста увеличивается, тем
самым начиная указывать на предыдущий элемент.

    --- Доказательство корректности ---
Из описания следует, что индекс tail будет всегда указывать на самую последнюю
ячейку в массиве, а head наоборот на самую первую. При удалении индексы просто
сдвигаются на предыдущий элемент, а переменная size не даст вылезти за рамки
массива или нарушить верное положение указателей головы и хвоста.

    --- Временная сложность ---
Добавление элемента будет выполняться за O(1), потому что добавление в массив
по индексу стоит O(1).
Извлечение элемента будет так же выполнятся за O(1), так как мы получаем
элемент по индексу, а потом просто сдвигаем индекс на единицу.

    --- Пространственная сложность ---
Данная реализация требует O(n) памяти, так как при инициализации мы создаём
массив размером n.
"""


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


def run_command(deque, name, value=None):
    command = getattr(deque, name)
    try:
        if value is None:
            return command()
        return command(value)
    except IndexError as error:
        return error


def run_commands(deque, commands):
    result = []
    for command in commands:
        command = command.split()
        if len(command) == 1:
            result.append(run_command(deque, command[0]))
            continue
        result.append(run_command(deque, command[0], int(command[1])))
    return '\n'.join(str(line) for line in result if line is not None)


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
