with open('poker.txt') as file:
    data = [line.split() for line in file.read().splitlines()]

values = {
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}
dummy_hands = {
    'royal flush': {
        'values': [11, 10, 12, 14, 13],
        'suits': ['H', 'H', 'H', 'H', 'H']
    },
    'straight flush': {
        'values': [11, 10, 12, 13, 9],
        'suits': ['S', 'S', 'S', 'S', 'S']
    },
    'four of a kind': {
        'values': [8, 9, 8, 8, 8],
        'suits': ['D', 'S', 'H', 'S', 'C']
    },
    'full house': {
        'values': [8, 9, 8, 9, 8],
        'suits': ['D', 'S', 'H', 'S', 'C']
    },
    'flush': {
        'values': [1, 9, 8, 9, 8],
        'suits': ['D', 'D', 'D', 'D', 'D']
    },
    'straight': {
        'values': [3, 5, 6, 4, 7],
        'suits': ['S', 'D', 'S', 'D', 'C']
    },
    'three of a kind': {
        'values': [3, 5, 6, 5, 5],
        'suits': ['S', 'D', 'S', 'D', 'C']
    },
    'two pairs': {
        'values': [3, 7, 3, 5, 5],
        'suits': ['S', 'D', 'S', 'D', 'C']
    },
    'one pair': {
        'values': [3, 7, 4, 5, 5],
        'suits': ['S', 'D', 'S', 'D', 'C']
    },
    'high card': {
        'values': [3, 7, 4, 1, 5],
        'suits': ['S', 'D', 'S', 'D', 'C']
    }
}


def separate_cards(hands):
    hands = [hands[0:5], hands[5:]]
    for idx, player in enumerate(hands):
        hands[idx] = {
            'values': [int(card[0]) if card[0] not in values else values.get(card[0]) for card in player],
            'suits': [card[1] for card in player]
        }
    return hands


def check_equal(hand: dict, key='suits', item_count=5, times=1, return_value=False):
    items: list = hand.get(key).copy()
    if times == 1:
        for item in items:
            if items.count(item) == item_count:
                return item if return_value else True
    else:
        found = []
        for item in items:
            if items.count(item) == item_count:
                for x in range(item_count):
                    items.remove(item)
                    found.append(item)
        if item_count * times + len(items) == 5:
            return found if return_value else True
    return False


def check_consecutive(hand: dict):
    items = sorted(hand.get('values'))
    for x in range(1, 5):
        if items[x] - 1 != items[x - 1]:
            return False
    return True


def assign_priority(hand: dict):
    """
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    Straight Flush: All cards are consecutive values of same suit.
    Four of a Kind: Four cards of the same value.
    Full House: Three of a kind and a pair.
    Flush: All cards of the same suit.
    Straight: All cards are consecutive values.
    Three of a Kind: Three cards of the same value.
    Two Pairs: Two different pairs.
    One Pair: Two cards of the same value.
    High Card: Highest value card.
    """
    # Royal Flush
    if check_equal(hand, 'suits') and all(value in hand.get('values') for value in values.values()):
        return 10
    # Straight Flush
    if check_equal(hand, 'suits') and check_consecutive(hand):
        return 9
    # Four Of A Kind
    if check_equal(hand, 'values', 4):
        return 8
    # Full House
    if check_equal(hand, 'values', 3) and check_equal(hand, 'values', 2):
        return 7
    # Flush
    if check_equal(hand, 'suits'):
        return 6
    # Straight
    if check_consecutive(hand):
        return 5
    # Three Of A Kind
    if check_equal(hand, 'values', 3):
        return 4
    # Two Pairs
    if check_equal(hand, 'values', 2, 2):
        return 3
    # One Pair
    if check_equal(hand, 'values', 2):
        return 2
    # High Card
    return 1


def untie(hands, priority):
    # One Pair
    if priority == 2:
        player1_pair = check_equal(hands[0], 'values', 2, return_value=True)
        player2_pair = check_equal(hands[1], 'values', 2, return_value=True)
        if player1_pair == player2_pair:
            player1_hand = sorted(hands[0].get('values').copy())
            player2_hand = sorted(hands[1].get('values').copy())
            for x in range(2):
                player1_hand.remove(player1_pair)
                player2_hand.remove(player2_pair)
            while player1_hand[-1] == player2_hand[-1]:
                del player1_hand[-1], player2_hand[-1]
            if player1_hand[-1] > player2_hand[-1]:
                return 11
        else:
            if player1_pair > player2_pair:
                return 11
        return 0
    # High Card
    if priority == 1:
        player1_pair = sorted(hands[0].get('values'))
        player2_pair = sorted(hands[1].get('values'))
        while player1_pair[-1] == player2_pair[-1]:
            del player1_pair[-1], player2_pair[-1]
        if player1_pair[-1] > player2_pair[-1]:
            return 11
        return 0


player1_wins, player2_wins = 0, 0
for game in data:
    players = separate_cards(game)
    player1_priority = assign_priority(players[0])
    player2_priority = assign_priority(players[1])

    if player1_priority == player2_priority:
        player1_priority = untie(players, player1_priority)
    if player1_priority > player2_priority:
        player1_wins += 1
    else:
        player2_wins += 1

print(f'{player1_wins = }, {player2_wins = }')
