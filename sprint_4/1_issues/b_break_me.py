def get_hash(codes, ground=1000, module=123987123):
    index = 0
    result = 0
    while index < len(codes) - 1:
        result += codes[index]
        result *= ground
        index += 1
    result += codes[index]
    result %= module
    return result


def get_codes(text):
    return [ord(char) for char in text]


def get_text(codes):
    return ''.join(chr(code) for code in codes)


if __name__ == '__main__':
    text = 'ezhgeljkablzwnvuwqvp'
    print(get_codes(text))
    text = 'gbpdcvkumyfxillgnqrv'
    print(get_codes(text))
    text = 'ehggggggg'
    print(get_hash(get_codes(text)))
    text = 'ggggbbbb'
    print(get_hash(get_codes(text)))
