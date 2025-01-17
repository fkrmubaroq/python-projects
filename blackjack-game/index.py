import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

def deal_card():
    """Return a random card from the deck"""
    card = random.choice(cards)
    return card

def initiate_deal_card():
    for _ in range(2):
        new_card = deal_card()
        user_cards.append(new_card)

