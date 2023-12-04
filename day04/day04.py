from day04input import input as inp

# A: too high; 48931, 23384 CORRECT: 21959
# B: CORRECT: 5132675
arr = [card.split(":")[1].strip().split('|') for card in inp.strip().split('\n')]


def get_wining_cards_amount(card):
    card_winning_points = 0
    card[0] = card[0].split(" ")
    card[1] = [str(x) for x in card[1].strip().split(" ") if x != ""]
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
    for i in range(len(arr)):
        card_winning_points = get_wining_cards_amount(arr[i])
        for j in range(1,card_winning_points+1):
            decks[i+j] += 1*decks[i]
    print(sum(decks))


day04a()
day04b()
