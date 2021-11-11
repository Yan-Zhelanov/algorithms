def determine_fours(num, array):
    history = set()
    array.sort()
    fours = set()
    for index_1 in range(len(array)):
        for index_2 in range(index_1+1, len(array)):
            for index_3 in range(index_2+1, len(array)):
                target = num - array[index_1] - array[index_2] - array[index_3]
                if target in history:
                    fours.add((
                        target, array[index_1], array[index_2], array[index_3]
                    ))
        history.add(array[index_1])
    return f'{len(fours)}\n' + '\n'.join(
        ' '.join(str(num) for num in item) for item in sorted(fours)
    )


def test_determine_fours():
    result = determine_fours(0, [1, 0, -1, 0, 2, -2])
    assert result == '3\n-2 -1 1 2\n-2 0 0 2\n-1 0 0 1', f'Wrong answer: {result}'
    result = determine_fours(10, [2, 3, 2, 4, 1, 10, 3, 0])
    assert result == '3\n0 3 3 4\n1 2 3 4\n2 2 3 3', f'Wrong answer: {result}'
    result = determine_fours(4668513, [-7795706, 4668513, 8226381, 3084315, -5622446, -890903, -5393660, -3853638, -9256234, 4721606, -3291023, -7147873, 7146058, -1472624, 2639816, -4680034, -5222739, 7162651, 2657843, -4959151, -3428252, -1759400, 9863878, 7042019, -8448507, 9846966, 8194959, -1524577, -8894866, 7391207, 4305956, 7903505, -6451721, 2146816, 104767, -376500, -6368075, -9578518, -2398899, 3290259, 2432261, -5267292, 514918, 253728, -1359195, 9074959, -2761227, 7725537, -7984728, -5804610, 499557, -6515724, -62490, -8214852, 5418214, -2538025, -1765082, 3606459, -4345495, 800482, -1634546, -2611283, 9411006, 299807, 5244500, 4177207, -6900412, -7320396, 5830526, -8878326, -5046919, 8281974, 1195361, 9130386, -5397774, -6593095, 8092421, 8708576, 9610647, 6324800, 1011549, -5458226, -9767835, 4241715, 1786996, 9280286, 7755890, 1320185, 5661335, -7874271, 5327400, 1315661, -882454, -2238334, 4925062, 2349773, 6139312, 758])
    assert result == '0\n', f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_determine_fours()
    # input()
    # print(determine_fours(int(input()), list(map(int, input().split()))))
