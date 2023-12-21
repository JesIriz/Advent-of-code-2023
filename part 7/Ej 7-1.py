from collections import Counter

card_dict = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 10,
    "Q": 11,
    "K": 12,
    "A": 13
}


def calculate_hand_value(hand_input):
    return int(card_dict[hand_input[0]]) * 13 ** 4 + \
        int(card_dict[hand_input[1]]) * 13 ** 3 + \
        int(card_dict[hand_input[2]]) * 13 ** 2 + \
        int(card_dict[hand_input[3]]) * 13 + \
        int(card_dict[hand_input[4]])


def is_five_of_a_kind(hand_input):
    return hand_input[0] == hand_input[1] == hand_input[2] == hand_input[3] == hand_input[4]


def is_four_of_a_kind(hand_input):
    hand_counter = Counter(hand_input)
    for count in hand_counter.values():
        if count == 4:
            return True

    return False


def is_full_house(hand_input):
    counter = {}
    for char in hand_input:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    values = list(counter.values())
    values.sort()

    if values == [2, 3]:
        return True
    else:
        return False


def is_three_of_a_kind(hand_input):
    hand_counter = Counter(hand_input)
    for count in hand_counter.values():
        if count == 3:
            return True

    return False


def is_two_pair(hand_input):
    counter = {}
    for char in hand_input:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    values = list(counter.values())
    values.sort()

    if values == [1, 2, 2]:
        return True
    else:
        return False


def is_one_pair(hand_input):
    counter = {}
    for char in hand_input:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    values = list(counter.values())
    values.sort()

    if values == [1, 1, 1, 2]:
        return True
    else:
        return False


def is_high_card(hand_input):
    counter = {}
    for char in hand_input:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    values = list(counter.values())
    values.sort()

    if values == [1, 1, 1, 1, 1]:
        return True
    else:
        return False


def hand_type_value(hand_input):
    if is_five_of_a_kind(hand_input):
        return 7
    if is_four_of_a_kind(hand_input):
        return 6
    if is_full_house(hand_input):
        return 5
    if is_three_of_a_kind(hand_input):
        return 4
    if is_two_pair(hand_input):
        return 3
    if is_one_pair(hand_input):
        return 2
    return 1


input_file = open('input_file.txt', 'r')
text = input_file.read()
lines = text.strip().split('\n')
hand_bid = [i.split() for i in lines]
hand_bid.sort(key=lambda x: calculate_hand_value(x[0]))

full_ordered_list = sorted(hand_bid, key=lambda x: (hand_type_value(x[0]), calculate_hand_value(x[0])))
print(full_ordered_list)

gain = 0
for index, hand in enumerate(full_ordered_list):
    rank = index + 1
    total_value = int(hand[1]) * rank
    gain += total_value

print(f"Las ganancias totales son: {gain}")
