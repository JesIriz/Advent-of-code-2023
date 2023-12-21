import re


def calculate_power(game_set):
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

    return max_red * max_green * max_blue 


input_file = open('input_file.txt', 'r')
count = 0

for line in input_file:
    line = line.split(": ")

    count += calculate_power(line[1])
    
print(f"El resultado es: {count}")    
