def getFirstDigit(input_text):
    for char in input_text:
        if char.isdigit():
            return str(char)
    return -1


def getLastDigit(input_text):
    for char in reversed(input_text):
        if char.isdigit():
            return str(char)
    return -1


def getCode(input_line):
    first_digit = getFirstDigit(input_line)
    last_digit = getLastDigit(input_line)
    return int(first_digit + last_digit)


input_file = open('input_file.txt', 'r')

count = 0

for line in input_file:
    code = getCode(line)
    count += code

print(f"El resultado es {count}")
