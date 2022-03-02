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
return counts for p1 and p2 after one stab played and who won the stab
p1 winner --> winner = 1
p2 winner --> winner = -1
input card of p1 & p2 as well as trump color and which player has to play first
first = 1 --> p1 plays
first = 0 --> p2 plays
"""


def stab(card_p1, card_p2, trump_color, turn):
    count_p1 = 0
    count_p2 = 0

    v_p1 = card_p1.value
    v_p2 = card_p2.value
    c_p1 = card_p1.color
    c_p2 = card_p2.color

    tr = 1
    return count_p1, count_p1, tr


def deck_not_empty(deck):
    return len(deck) != 0


def game(deck):
    p1 = Player(input("Give P1 a name: "))
    p2 = Player(input("Give P2 a name: "))
    turn = 1        #since p1 gets the first card
    for i in range(5):
        p1.hand.append(draw_card(deck))
        p2.hand.append(draw_card(deck))

    trump_value, trump_color = determine_trump(deck)
    trump = deck.pop()
    deck.insert(0, trump)   #adding the trump card to the bottom of the stack since it is the last card and openly
                            #seen to all players

    while deck_not_empty(deck):
        print(p1.hand)
        print(p2.hand)
        card_played_p1 = int(input(p1.name + " Welche karte willst du spielen bitte index startend von 0: "))
        card_played_p2 = int(input(p2.name + " Welche karte willst du spielen bitte index startend von 0: "))

        p1.count, p2.count, turn = stab(p1.hand[card_played_p1], p2.hand[card_played_p2], trump_color, turn)
        p1.hand.pop(card_played_p1)
        p2.hand.pop(card_played_p2)

        if turn:
            p1.hand.append(draw_card(deck))
            p2.hand.append(draw_card(deck))
        else:
            p2.hand.append(draw_card(deck))
            p1.hand.append(draw_card(deck))


    print(trump_color)
    print(trump_value)




deck_66 = build_Deck()
game(deck_66)
