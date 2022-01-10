from random import randint


def get_hash(codes, ground=1000, module=123987123):
    index = 0
    result = 0
    size = len(codes) - 1
    while index < size:
        result = (((result + codes[index]) % module) * ground) % module
        index += 1
    result = (result + codes[index]) % module
    return result


def get_codes(text):
    return [ord(char) for char in text]


def get_text(codes):
    return ''.join(chr(code) for code in codes)


def parse(text):
    expected_hash = get_hash(get_codes(text))
    result = 'aaaaaaaa'
    result = get_codes(result)
    size = len(result) - 1
    while True:
        result[randint(0, size)] = randint(97, 122)
        if get_hash(result) == expected_hash:
            return get_text(result)


if __name__ == '__main__':
    # text = 'ezhgeljkablzwnvuwqvp'
    # print(get_codes(text))
    # text = 'gbpdcvkumyfxillgnqrv'
    # print(get_codes(text))
    text = 'eyshdgsx'
    print(parse(text))
