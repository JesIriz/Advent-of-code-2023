import re


def getMatches(input_line, match_list_input):
    regex = '|'.join(map(re.escape, match_list_input))
    regex = '(?=(' + regex + '))'

    matches = re.findall(regex, input_line)

    return matches


def transformMatches(input_list):
    number_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    result = []
    for el in input_list:
        if el in number_map:
            result.append(number_map[el])
        else:
            result.append(el)

    return result


def getNumbers(input_line, match_list_input):
    matches = getMatches(input_line, match_list_input)
    return transformMatches(matches)


input_file = open('input_file.txt', 'r')
match_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
              'eight', 'nine']

count = 0

for line in input_file:
    numbers = getNumbers(line, match_list)
    firstDigit = numbers[0]
    lastDigit = numbers[-1]
    code = int(firstDigit + lastDigit)
    count += code

print(f"El resultado es {count}")
