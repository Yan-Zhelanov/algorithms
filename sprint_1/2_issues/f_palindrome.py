def determine_palindrome(text):
    text = ''.join(char if char.isalpha() else '' for char in text.lower())
    return True if text == ''.join(reversed(text)) else False


def test_determine_palindrome():
    assert determine_palindrome('A man, a plan, a canal: Panama') == True
    assert determine_palindrome('zo') == False
    assert determine_palindrome('z') == True
    assert determine_palindrome('zooz') == True
    assert determine_palindrome('zozo') == False
    print('Все тесты пройдены!')


if __name__ == '__main__':
    print(determine_palindrome(input()))
