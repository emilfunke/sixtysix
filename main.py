from random import shuffle
"""
player having a list of cards in hand and a count of tricks made by player
"""


class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.count = 0


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
            card = "{}, {}".format(c, v)
            deck.append(card)
    shuffle(deck)
    return deck


def draw_card(deck):
    return deck.pop()


def determine_trump(deck):
    trump_card = deck.pop()
    trump_color = ""
    for i in range(len(trump_card)):
        if trump_card[i] != ",":
            trump_color += trump_card[i]
        else:
            break
    return trump_color, trump_card

def game(deck):
    p1 = Player(input("Give P1 a name: "))
    p2 = Player(input("Give P2 a name: "))

    for i in range(5):
        p1.hand.append(draw_card(deck_66))
        p2.hand.append(draw_card(deck_66))

    trump_color, trump_card = determine_trump(deck_66)

    print(p1.hand)

    print(trump_color)
    print(trump_card)


deck_66 = build_Deck()
game(deck_66)

