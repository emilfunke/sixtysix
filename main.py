from random import shuffle
"""
player having a list of cards in hand and a count of tricks made by player
"""


class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.count = 0

class Card():
    def __init__(self, value, color):
        self.value = value
        self.color = color
"""
create the 52 card deck and shuffle it
return: shuffled deck -> list
input: none
"""


def build_Deck():
    deck = []
    # card of the form (color, value)
    color = ["Eichel", "Grün", "Herz", "Schell"]
    value = [7, 8, 9, 10, 2, 3, 4, 11]

    for c in color:
        for v in value:
            card = Card(v, c)
            deck.append(card)
    shuffle(deck)
    return deck


def draw_card(deck):
    return deck.pop()

"""
returns the trump card value and color in that order
"""
def determine_trump(deck):
    trump_card = deck.pop()
    return trump_card.value, trump_card.color

"""
return counts for p1 and p2 after one stab played
input card of p1 & p2 as well as trump color and which player has to play first
first = 1 --> p1 plays
first = -1 --> p2 plays
"""
def stab(card_p1, card_p2, trump_color, first):
    count_p1 = 0
    count_p2 = 0

    v_p1 = card_p1.value
    v_p2 = card_p2.value
    c_p1 = card_p1.color
    c_p2 = card_p2.color



def game(deck):
    p1 = Player(input("Give P1 a name: "))
    p2 = Player(input("Give P2 a name: "))

    for i in range(5):
        p1.hand.append(draw_card(deck_66))
        p2.hand.append(draw_card(deck_66))

    trump_value, trump_color = determine_trump(deck_66)

    print(p1.hand)
    print(p2.hand)


    print(trump_color)
    print(trump_value)

    stab(p1.hand.pop(), p2.hand.pop(), trump_color, 1)


deck_66 = build_Deck()
game(deck_66)

