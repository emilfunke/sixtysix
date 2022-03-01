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
    value = [7, 8, 9, 10, "2", "3", "4", 11]

    for c in color:
        for v in value:
            card = Card(v, c)
            deck.append(card)
    shuffle(deck)
    return deck


def draw_card(deck):
    return deck.pop()


def determine_trump(deck):
    trump_card = deck.pop()
    return trump_card.value, trump_card.color

def stab(card_p1, card_p2, trump_color):
    count_p1 = 0
    count_p2 = 0

    v_p1 = card_p1.value
    v_p2 = card_p2.value
    c_p1 = card_p1.color
    c_p2 = card_p2.color


    if (c_p2 != trump_color & c_p1 != trump_color):
        if v_p1 > v_p2:
            return v_p1+v_p2, 0
        elif v_p2 > v_p1:
            return 0, v_p1+v_p2


    return count_p1, count_p2

def game(deck):
    p1 = Player(input("Give P1 a name: "))
    p2 = Player(input("Give P2 a name: "))

    for i in range(5):
        p1.hand.append(draw_card(deck_66))
        p2.hand.append(draw_card(deck_66))

    trump_color, trump_card = determine_trump(deck_66)

    print(p1.hand)
    print(p2.hand)


    print(trump_color)
    print(trump_card)

    stab(p1.hand.pop(), p2.hand.pop(), trump_color)


deck_66 = build_Deck()
game(deck_66)

