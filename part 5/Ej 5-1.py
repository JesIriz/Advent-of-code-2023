def map_to_matrix(input_lines):
    return [list(map(int, line.split())) for line in input_lines]


def find_number_in_map(number, map_to_test):
    for map_entry in map_to_test:
        if int(map_entry[1]) <= number < map_entry[1] + map_entry[2]:
            return map_entry[0] + (number - map_entry[1])
    return number


input_file = open('input_file.txt', 'r')
count = 0

text = input_file.read()
lines = text.strip().split('\n\n')

seeds = lines[0][7:].split(' ')

seed_to_soil_map = map_to_matrix(lines[1].split('\n')[1:])
soil_to_fertilizer_map = map_to_matrix(lines[2].split('\n')[1:])
fertilizer_to_water_map = map_to_matrix(lines[3].split('\n')[1:])
water_to_light_map = map_to_matrix(lines[4].split('\n')[1:])
light_to_temperature_map = map_to_matrix(lines[5].split('\n')[1:])
temperature_to_humidity_map = map_to_matrix(lines[6].split('\n')[1:])
humidity_to_location_map = map_to_matrix(lines[7].split('\n')[1:])

locations = []
for seed in seeds:
    soil = find_number_in_map(int(seed), seed_to_soil_map)
    fertilizer = find_number_in_map(soil, soil_to_fertilizer_map)
    water = find_number_in_map(fertilizer, fertilizer_to_water_map)
    light = find_number_in_map(water, water_to_light_map)
    temperature = find_number_in_map(light, light_to_temperature_map)
    humidity = find_number_in_map(temperature, temperature_to_humidity_map)
    location = find_number_in_map(humidity, humidity_to_location_map)

    locations.append(location)

print(f"La location minima es: {min(locations)}")
