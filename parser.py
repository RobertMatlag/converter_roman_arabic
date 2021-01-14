def parse_roman_numeral(s):
    roman_arabic_dict = {'I': 1}

    index = 0
    value = 0
    while index < len(s):
        sign = s[index]
        value += roman_arabic_dict[sign]
        index += 1

    return value


if __name__ == '__main__':
    pass
