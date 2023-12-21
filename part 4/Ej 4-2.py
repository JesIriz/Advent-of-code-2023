
input_file = open('input_file.txt', 'r')
count = 0

text = input_file.read()
lines = text.strip().split('\n')
card_amounts = [1] * len(lines)

for index, line in enumerate(lines):
    cards_info = line.split(': ')[1]
    splitted_cards = cards_info.split('|')
    
    prize_numbers = [x.strip() for x in splitted_cards[0].strip().replace('  ', ' ').split(' ')]
    my_numbers = [x.strip() for x in splitted_cards[1].strip().replace('  ', ' ').split(' ')]

    matches = set(prize_numbers) & set(my_numbers)
    matched_elements = len(matches)

    for x in range(index + 1, index + matched_elements + 1):
        card_amounts[x] += card_amounts[index]
    
print(f"final value: {sum(card_amounts)}")
