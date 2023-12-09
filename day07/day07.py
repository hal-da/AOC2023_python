import functools
from day07data import data as inp

inp = [card.split(" ") for card in inp.split('\n')]


# CORRECT A: 247815719, CORRECT B: 248747492

def get_card_value_puzzle_a(card: str) -> int:
    card = sorted(card)
    value = 1
    acc = 1
    for i in range(0, len(card) - 1):
        if card[i + 1] == card[i]:
            acc *= 2
            value += value * acc
        else:
            acc = 1
    return value


def get_card_value_puzzle_b(cards: str) -> int:
    cards = sorted(cards.replace("J", ""))
    if not bool(cards):
        cards = "11111"
    value = 1
    acc = 1
    my_cards = {}
    for card in cards:
        if card in my_cards:
            my_cards[card] += 1
        else:
            my_cards[card] = 1
    most_common_card = next(iter(dict(sorted(my_cards.items(), key=lambda item: item[1], reverse=True))))
    amount_of_missing_cards = 5 - len(cards)
    if amount_of_missing_cards > 0:
        cards += [most_common_card] * amount_of_missing_cards
        cards = sorted(cards)

    for i in range(0, len(cards) - 1):
        if cards[i + 1] == cards[i]:
            acc *= 2
            value += value * acc
        else:
            acc = 1
    return value


# A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2.
my_dict_puzzle_a = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3,
                    "2": 2}
my_dict_puzzle_b = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3,
                    "2": 2}


class Sorting:
    def __init__(self, my_dict):
        self.my_dict = my_dict

    def sort_by_card(self, a, b):
        if a[2] == b[2]:
            a = [self.my_dict[x] for x in a[0]]
            b = [self.my_dict[x] for x in b[0]]
            if a > b:
                return 1
            elif a < b:
                return -1
            return 0

        if a[2] > b[2]:
            return 1
        elif a[2] < b[2]:
            return -1
        return 0


def puzzle_a(inp_a):

    sort_by_card = Sorting(my_dict_puzzle_a)
    for card in inp_a:
        card.append(get_card_value_puzzle_a(card[0]))
    inp_a = sorted(inp_a, key=functools.cmp_to_key(sort_by_card.sort_by_card))
    inp_a = [(i + 1) * int(card[1]) for i, card in enumerate(inp_a)]
    print(sum(inp_a))


def puzzle_b(inp_b):

    sort_by_card_b = Sorting(my_dict_puzzle_b)
    for card in inp_b:
        card.append(get_card_value_puzzle_b(card[0]))
    inp_b = sorted(inp_b, key=functools.cmp_to_key(sort_by_card_b.sort_by_card))
    inp_b = [(i + 1) * int(card[1]) for i, card in enumerate(inp_b)]
    print(sum(inp_b))


# puzzle_a(inp)
puzzle_b(inp)
