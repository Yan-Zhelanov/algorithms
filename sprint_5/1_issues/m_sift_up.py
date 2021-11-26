def sift_up(heap, index):
    if index == 1:
        return index
    parent = index // 2
    if heap[parent] > heap[index]:
        return index
    heap[parent], heap[index] = heap[index], heap[parent]
    return sift_up(heap, parent)


def test_sift_up():
    result = sift_up([-1, 12, 6, 8, 3, 15, 7], 5)
    assert result == 1, f'Wrong answer: {result}'
    result = sift_up([-1, 12, 6, 8, 3, 2, 9], 6)
    assert result == 3, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_sift_up()
