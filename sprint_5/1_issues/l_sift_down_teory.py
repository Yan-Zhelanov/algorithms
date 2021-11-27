def sift_down(heap, index):
    size = len(heap) - 1
    left = index * 2
    right = index * 2 + 1
    if left > size:
        return index
    if right <= size and heap[left] < heap[right]:
        largest_index = right
    else:
        largest_index = left
    if heap[index] < heap[largest_index]:
        heap[largest_index], heap[index] = heap[index], heap[largest_index]
        return sift_down(heap, largest_index)
    return index


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
