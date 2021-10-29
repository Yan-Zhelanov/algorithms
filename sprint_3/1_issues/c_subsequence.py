# class Queue:
#     def __init__(self, max_size):
#         self.max_size = max_size
#         self.queue = [None] * max_size
#         self.size = 0
#         self.tail = 0
#         self.head = 0

#     def is_empty(self):
#         return self.size == 0

#     def is_max(self):
#         return self.size == self.max_size

#     def push(self, value):
#         if self.is_max():
#             raise IndexError('error')
#         self.queue[self.head] = value
#         self.head = (self.head + 1) % self.max_size
#         self.size += 1

#     def pop(self):
#         if self.is_empty():
#             raise IndexError('error')
#         previous = self.tail
#         self.tail = (self.tail + 1) % self.max_size
#         self.size -= 1
#         return self.queue[previous]


# def is_subsequence(sequence, text):
#     if sequence == '':
#         return True
#     queue = Queue(len(sequence))
#     for char in sequence:
#         queue.push(char)
#     temp = queue.pop()
#     for char in text:
#         if char == temp:
#             try:
#                 temp = queue.pop()
#             except IndexError:
#                 return True
#     return False


def is_subsequence(sequence, text):
    if sequence == '':
        return True
    index_sequence = index_text = 0
    while index_sequence < len(sequence) and index_text < len(text):
        if sequence[index_sequence] == text[index_text]:
            index_sequence += 1
        index_text += 1
    if index_sequence == len(sequence):
        return True
    return False


def test_is_subsequence():
    result = is_subsequence('abc', 'ahbgdcu')
    assert result, f'Wrong answer: {result}'
    result = is_subsequence('aaa', 'abc')
    assert not result, f'Wrong answer: {result}'
    result = is_subsequence('aaa', 'aaaaa')
    assert result, f'Wrong answer: {result}'
    result = is_subsequence('aked', 'asdek')
    assert not result, f'Wrong answer: {result}'
    result = is_subsequence('a', 'a')
    assert result, f'Wrong answer: {result}'
    result = is_subsequence('a', 'b')
    assert not result, f'Wrong answer: {result}'
    result = is_subsequence('a', 'aa')
    assert result, f'Wrong answer: {result}'
    result = is_subsequence('', 'aa')
    assert result, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_is_subsequence()
    print(is_subsequence(input(), input()))
