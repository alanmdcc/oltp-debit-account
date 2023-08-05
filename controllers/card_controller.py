from schemas.account import Account
from schemas.card import Card

from typing import Union


class CardController:
    # create
    @staticmethod
    def create_card(
            account: Account,
            name: str,
            cvv: str):
        card = Card(account_id=account.id, name=name, cvv=cvv)
        card.save()
        return card

    # read
    @staticmethod
    def get_card_by_id(id: int) -> Union[Card, None]:
        try:
            return Card.get(id=id)
        except:
            return None

    @staticmethod
    def get_card_by_account(account: Account) -> Union[Card, None]:
        try:
            return Card.get(account_id=account.id)
        except Card.DoesNotExist:
            return None

    # cannot update data of a card

    # delete
    @staticmethod
    def delete_card(card: Card):
        account = Account.get(id=card.account_id)
        balance = account.balance
        if balance == 0:
            print(f'Card with ID={card.id} was deleted')
            card.delete_instance()
        else:
            print('Balance must be zero')
