"""Import statements"""
from Database.database import Database


class Card:
    """card class to store details of the card"""

    def __init__(self, card_id, user_id, card_number, cvv):
        self.card_id = card_id
        self.user_id = user_id
        self.card_number = card_number
        self.cvv = cvv
        self.datab = Database()

    def __str__(self):
        return f"Card Number:XXXX XXXX XXXX {str(self.card_number)[12:]}"

    @staticmethod
    def fetch_all_cards():
        """fetching all card details"""
        card_list = Database().fetch_all_cards()
        cards = []
        for card in card_list:
            cards.append(Card(card[0], card[1], card[2], card[3]))
        return cards
