
def map_to_matrix(input_lines):
    return [list(map(int, line.split())) for line in input_lines]


def inverse_mapping(number, map_to_test):
    for map_entry in map_to_test:
        if map_entry[0] <= number <= map_entry[0] + map_entry[2]:
            return map_entry[1] + (number - map_entry[0])
    return number


input_file = open('input_file.txt', 'r')
count = 0

text = input_file.read()
lines = text.strip().split('\n\n')

seed_to_soil_map = map_to_matrix(lines[1].split('\n')[1:])
soil_to_fertilizer_map = map_to_matrix(lines[2].split('\n')[1:])
fertilizer_to_water_map = map_to_matrix(lines[3].split('\n')[1:])
water_to_light_map = map_to_matrix(lines[4].split('\n')[1:])
light_to_temperature_map = map_to_matrix(lines[5].split('\n')[1:])
temperature_to_humidity_map = map_to_matrix(lines[6].split('\n')[1:])
humidity_to_location_map = map_to_matrix(lines[7].split('\n')[1:])


def full_inverse_mapping(location_to_map):
    humidity = inverse_mapping(location_to_map, humidity_to_location_map)
    temperature = inverse_mapping(humidity, temperature_to_humidity_map)
    light = inverse_mapping(temperature, light_to_temperature_map)
    water = inverse_mapping(light, water_to_light_map)
    fertilizer = inverse_mapping(water, fertilizer_to_water_map)
    soil = inverse_mapping(fertilizer, soil_to_fertilizer_map)
    seed = inverse_mapping(soil, seed_to_soil_map)

    return seed


def seeds_as_ranges_calculation(seeds_to_map):
    calculated_seeds = []
    range_start = 0
    for index, seed in enumerate(seeds_to_map):
        if index % 2 == 0:
            range_start = int(seed)
        else:
            calculated_seeds.append((range_start, range_start + int(seed) - 1))

    return calculated_seeds


def seed_in_list(seed_to_find, ranges):
    for r in ranges:
        if r[0] <= seed_to_find <= r[1]:
            return True

    return False


seeds = lines[0][7:].split(' ')

seeds_as_ranges = seeds_as_ranges_calculation(seeds)
print(seeds_as_ranges)

finished = False
location = 1
while not finished:
    seed_from_location = full_inverse_mapping(location)
    if seed_in_list(seed_from_location, seeds_as_ranges):
        print(f"La location minima es: {location}")
        finished = True
    else:
        location += 1
