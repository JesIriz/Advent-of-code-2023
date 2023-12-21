import re
import numpy


def extract_submatrix(matriz, esquina_superior_izquierda, esquina_inferior_derecha):
    columna_inicio, fila_inicio = esquina_superior_izquierda
    columna_fin, fila_fin = esquina_inferior_derecha

    submatriz = [fila[columna_inicio:columna_fin + 1] for fila in matriz[fila_inicio:fila_fin + 1]]

    return submatriz


def index_to_position(index, size):
    return index // size, index % size


def span_to_area(span, matrix_size):
    number_first_pos = index_to_position(span[0], matrix_size[1])
    number_last_pos = index_to_position(span[1], matrix_size[1])

    area_first_pos_x = 0
    area_first_pos_y = 0
    if number_first_pos[0] > 0:
        area_first_pos_x = number_first_pos[0] - 1
    if number_first_pos[1] > 0:
        area_first_pos_y = number_first_pos[1] - 1
    area_first_pos = (area_first_pos_y, area_first_pos_x)

    area_last_pos_x = matrix_size[0]
    area_last_pos_y = matrix_size[1]
    if number_last_pos[0] < matrix_size[0]:
        area_last_pos_x = number_last_pos[0] + 1
    if number_last_pos[1] < matrix_size[1]:
        area_last_pos_y = number_last_pos[1] + 1
    area_last_pos = (area_last_pos_y, area_last_pos_x)

    return area_first_pos, area_last_pos


def find_number_matches(input_text):
    number_matches = re.finditer(r'\d+', input_text)
    return number_matches


def has_gear(sb_matrix, upper_corner_gear, num_value):
    for rowi, row in enumerate(sb_matrix):
        for coli, el in enumerate(row):
            if el == '*':
                return {"has_gear": True, "gear_pos": (upper_corner_gear[0] + coli, upper_corner_gear[1] + rowi),
                        "num_value": num_value}
    return {"has_gear": False, "gear_pos": (-1, -1), "num_value": num_value}


input_file = open('input_file.txt', 'r')

text = input_file.read()
lines = text.strip().split('\n')
matrix = [list(line) for line in lines]
matrix_shape = numpy.shape(matrix)

numbers = find_number_matches(text.replace('\n', ''))

count = 0
help_list = []

for number in numbers:
    real_span = (number.span()[0], number.span()[1] - 1)
    area = span_to_area(real_span, matrix_shape)
    upper_corner = area[0]
    lower_corner = area[1]
    submatrix = extract_submatrix(matrix, upper_corner, lower_corner)
    number_has_gear = has_gear(submatrix, upper_corner, int(number.group()))

    if number_has_gear["has_gear"]:
        agregar = True
        for elemento in help_list:
            if elemento["gear_pos"] == number_has_gear["gear_pos"]:
                agregar = False
                help_list.remove(elemento)
                count += elemento["num_value"] * number_has_gear["num_value"]
                break
        if agregar:
            help_list.append(number_has_gear)

print(f"count total: {count}")
