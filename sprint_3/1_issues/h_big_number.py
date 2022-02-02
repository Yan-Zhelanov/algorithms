from functools import cmp_to_key


def compare(num_1, num_2):
    if num_1 == num_2:
        return 0
    num_1, num_2 = int(num_1+num_2), int(num_2+num_1)
    if num_1 < num_2:
        return -1
    return 1


def determine_biggest_number(array):
    array.sort(key=cmp_to_key(compare), reverse=True)
    return ''.join(array)


def test_determine_biggest_number():
    result = determine_biggest_number(['15'])
    assert result == '15', f'Wrong answer: {result}'
    result = determine_biggest_number(['1', '5'])
    assert result == '51', f'Wrong answer: {result}'
    result = determine_biggest_number(['15', '56', '2'])
    assert result == '56215', f'Wrong answer: {result}'
    result = determine_biggest_number(['1', '99', '100'])
    assert result == '991100', f'Wrong answer: {result}'
    result = determine_biggest_number(['1', '1', '1', '100', '5'])
    assert result == '5111100', f'Wrong answer: {result}'
    result = determine_biggest_number(['99', '1', '99', '100', '1', '5'])
    assert result == '9999511100', f'Wrong answer: {result}'
    result = determine_biggest_number(['823', '828', '825', '828'])
    assert result == '828828825823', f'Wrong answer: {result}'
    result = determine_biggest_number(['8', '28', '828'])
    assert result == '882828', f'Wrong answer: {result}'
    result = determine_biggest_number(['82', '825', '8'])
    assert result == '882825', f'Wrong answer: {result}'
    result = determine_biggest_number(['825', '8', '28', '828', '25', '5'])
    assert result == '882882552825', f'Wrong answer: {result}'
    result = determine_biggest_number(['825', '823', '8', '8', '828', '825', '828', '828', '82'])  # noqa
    assert result == '8882882882882825825823', f'Wrong answer: {result}'
    nums = '82 468 941 181 287 861 291 515 263 424 470 620 954 894 565 69 148 587 823 57 730 389 921 1000 447 1000 748 104 831 943 174 24 340 1000 150 937 324 919 748 271 980 575 392 779 222 316 944 1000 160 501 319 436 26 828 348 211 825 857 486 1000 419 509 409 679 576 700 418 810 674 83 785 251 947 868 964 384 497 192 1000 998 756 649 269 290 197 30 95 796 642 980 474 122 443 707 839 213 1000 530 263 193' # noqa
    expected = '99898098096495954947944943941937921919894868861857839838318288282582381079678577975674874873070770069679674649642620587576575755655305155095014974864744704684474434364244194184093923893843483403243193163029129028727126926326326251242222132111971931921811741601501481221041000100010001000100010001000' # noqa
    result = determine_biggest_number(nums.split())
    assert result == expected, f'Wrong answer: {result}'
    print('All tests passed!')


if __name__ == '__main__':
    test_determine_biggest_number()
    input()
    print(determine_biggest_number(input().split()))
