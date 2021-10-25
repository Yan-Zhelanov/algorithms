class Stack:
    BRACKETS = {
        '{': '}',
        '[': ']',
        '(': ')',
    }

    def __init__(self):
        self.stack = []

    def push(self, bracket):
        self.stack.append(self.BRACKETS[bracket])

    def pop(self, bracket):
        if bracket != self.stack[-1]:
            raise ValueError('error')
        self.stack.pop()

    def get_length(self):
        return len(self.stack)


def is_correct_bracket_seq(sequence):
    brackets = Stack()
    for bracket in sequence:
        if bracket in brackets.BRACKETS:
            brackets.push(bracket)
            continue
        try:
            brackets.pop(bracket)
        except (ValueError, IndexError):
            return False
    if brackets.get_length() > 0:
        return False
    return True


def test_is_correct_bracket_seq():
    result = is_correct_bracket_seq('{{{)))')
    assert not result
    result = is_correct_bracket_seq('((()))')
    assert result
    result = is_correct_bracket_seq('{}()[][[()]]')
    assert result
    result = is_correct_bracket_seq('[{](})()[][[()]]')
    assert not result
    result = is_correct_bracket_seq('[[[[]]]')
    assert not result
    result = is_correct_bracket_seq(']]]]')
    assert not result
    result = is_correct_bracket_seq('[([(')
    assert not result
    print('Все тесты пройдены!')


if __name__ == '__main__':
    # test_is_correct_bracket_seq()
    print(is_correct_bracket_seq(input()))
