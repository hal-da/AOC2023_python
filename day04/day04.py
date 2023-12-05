from day04input import input as inp

# A: too high; 48931, 23384 CORRECT: 21959
# B: CORRECT: 5132675
arr = [card.split(":")[1].strip().split('|') for card in inp.strip().split('\n')]

# for future reference:
# https://github.com/evanphoward/AdventOfCode/blob/main/AOC_23/Day4/main.py
# inp = open("input").read().split("\n")
# inp = [[[int(y) for y in x.split("|")[0].split(":")[1].split()], [int(y) for y in x.split("|")[1].split()]] for x in inp]
# ans = 0
#
# cards = [1 for _ in range(len(inp))]
#
# for i, (winning, have_num) in enumerate(inp):
#     matches = sum(num in have_num for num in winning)
#     pts = 0 if matches == 0 else 2 ** (matches - 1)
#     ans += pts
#     for j in range(i + 1, i + matches + 1):
#         cards[j] += cards[i]
#
# print("Part 1:", ans)
# print("Part 2:", sum(cards))

#    DR. TONTAFEL
#     dataset = [[[a for a in line.split("|")[0].split(": ")[1].strip().split(" ") if a], [b for b in line.split("|")[1].split("\n")[0].strip().split(" ") if b]] for line in f]


def get_wining_cards_amount(card):
    card_winning_points = 0
    card[0] = card[0].split(" ")
    card[1] = [str(x) for x in card[1].strip().split(" ") if x]
    for winning_nums in card[0]:
        try:
            card[1].index(winning_nums)
            card_winning_points += 1
        except:
            continue
    card[0] = " ".join(card[0])
    card[1] = " ".join(card[1])
    return card_winning_points


def day04a():
    overall_winning_points = 0
    for card in arr:
        card_winning_points = get_wining_cards_amount(card)
        if card_winning_points > 0:
            overall_winning_points += pow(2, (card_winning_points - 1))
    print(overall_winning_points)


def day04b():
    decks = [1]*len(arr)
    for i, _ in enumerate(arr):
        card_winning_points = get_wining_cards_amount(arr[i])
        for j in range(1,card_winning_points+1):
            decks[i+j] += 1*decks[i]
    print(sum(decks))


day04a()
day04b()
