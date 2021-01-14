import re


# pattern = re.compile(r'^[I]{1,3}$')
# matches = pattern.finditer(s)
# match = next(matches)
# print(match)

def parse_roman_numeral(s):
    roman_arabic_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50}

    index = 0
    value = 0
    while index < len(s):
        sign = s[index]
        if index == len(s) - 1:
            value += roman_arabic_dict[sign]
            index += 1
        else:
            next_sign = s[index + 1]
            first_value = roman_arabic_dict[sign]
            second_value = roman_arabic_dict[next_sign]

            if second_value > first_value:
                value += (second_value - first_value)
                index += 2
            else:
                value += roman_arabic_dict[sign]
                index += 1

    return value


if __name__ == '__main__':
    pass
