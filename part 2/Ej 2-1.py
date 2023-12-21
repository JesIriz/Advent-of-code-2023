import re


def isValid(game_set):
    game_set = game_set.strip()
    splitted_set_list = re.split('; |, | ', game_set)

    max_green = 0
    max_red = 0
    max_blue = 0
    
    for index, el in enumerate(splitted_set_list):
        prev_el = splitted_set_list[index-1]
        if el == "green" and int(prev_el) > max_green:
            max_green = int(prev_el)
        elif el == "red" and int(prev_el) > max_red:
            max_red = int(prev_el)
        elif el == "blue" and int(prev_el) > max_blue:
            max_blue = int(prev_el)

    return max_red <= 12 and max_green <= 13 and max_blue <= 14


input_file = open('input_file.txt', 'r')
count = 0

for line in input_file:
    line = line.split(": ")

    if isValid(line[1]):
        count += int(line[0][5:])
    
print(f"El resultado es: {count}")    
