
input_file = open('input_file.txt', 'r')
count = 0

text = input_file.read()
lines = text.strip().split('\n')

for line in lines:
    cards_info = line.split(': ')[1]
    splitted_cards = cards_info.split('|')
    
    prize_numbers = [x.strip() for x in splitted_cards[0].strip().replace('  ', ' ').split(' ')]
    my_numbers = [x.strip() for x in splitted_cards[1].strip().replace('  ', ' ').split(' ')]

    matches = set(prize_numbers) & set(my_numbers)
    matched_elements = len(set(prize_numbers) & set(my_numbers))
    if matched_elements > 0:
        value = pow(2, matched_elements - 1)
        count += value
    
print(f"final count: {count}")
