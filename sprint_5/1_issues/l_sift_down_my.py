def sift_down(heap, index):
    size = len(heap) - 1
    if index == size:
        return index
    left = index * 2
    right = index * 2 + 1
    largest_index = 0
    if right <= size and heap[right] > heap[left] > heap[index]:
        largest_index = right
    elif left <= size and heap[left] > heap[index]:
        largest_index = left
    if largest_index == 0:
        return index
    heap[largest_index], heap[index] = heap[index], heap[largest_index]
    return sift_down(heap, largest_index)


def test_sift_down():
    result = sift_down([-1, 12, 1, 8, 3, 4, 7], 2)
    assert result == 5, f'Wrong answer: {result}'
    result = sift_down([-1, 1, 12, 8, 3, 4, 7], 1)
    assert result == 5, f'Wrong answer: {result}'
    result = sift_down([-1, 12, 11, 2, 3, 4, 7, 8], 3)
    assert result == 7, f'Wrong answer: {result}'
    result = sift_down([-1, 12, 11, 9, 3, 4, 7, 8, 6, 5], 4)
    assert result == 8, f'Wrong answer: {result}'
    result = sift_down([-1, 10, 9, 8, 3, 4, 7, 1], 1)
    assert result == 1, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_sift_down()
