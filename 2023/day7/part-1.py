def map_hand_to_number(hand):
    card_map = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
    return [int(card_map.get(card, card)) for card in hand]


def evaulate_hand(hand):
    def score(hand, base_score):
        total_score = base_score * 16**5
        for i, card in enumerate(hand):
            total_score += card * (16 ** (4 - i))

        return total_score

    counter = {}
    for card in hand:
        counter[card] = hand.count(card)
    # Five of a kind
    if 5 in counter.values():
        return score(hand, 6)
    # Four of a kind
    if 4 in counter.values():
        return score(hand, 5)
    # Full house
    if 3 in counter.values() and 2 in counter.values():
        return score(hand, 4)
    # Three of a kind
    if 3 in counter.values():
        return score(hand, 3)
    # Two pairs
    if list(counter.values()).count(2) == 2:
        return score(hand, 2)
    # One pair
    if 2 in counter.values():
        return score(hand, 1)
    # High card
    return score(hand, 0)


with open("input.txt", "r") as file:
    lines = file.read().splitlines()

hands = [line.split(" ") for line in lines]
hands = [(hand[0], int(hand[1])) for hand in hands]
hands = [(map_hand_to_number(hand), bid) for hand, bid in hands]
hands = sorted(hands, key=lambda x: evaulate_hand(x[0]))

total_winnings = sum(rank * bid for rank, (hand, bid) in enumerate(hands, start=1))
print(total_winnings)
