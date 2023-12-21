import math


def number_of_cases(a, b):
    higher_int = math.ceil(b)
    lower_int = math.floor(a)
    return abs(higher_int - lower_int) - 1 if higher_int > lower_int else 0


input_file = open('input_file.txt', 'r')
text = input_file.read()
lines = text.strip().split('\n')
tt_list = [int(x) for x in lines[0].strip().split()[1:]]
r_list = [int(x) for x in lines[1].strip().split()[1:]]

tt = int(''.join([str(x) for x in tt_list]))
r = int(''.join([str(x) for x in r_list]))

lower_limit = (-tt + (tt ** 2 - 4 * r) ** 0.5) / -2
upper_limit = (-tt - (tt ** 2 - 4 * r) ** 0.5) / -2
cases = number_of_cases(lower_limit, upper_limit)

print(f"Hay {cases} casos posibles")
