import datetime

from schemas.account import Account
from schemas.card import Card
from schemas.transaction import Transaction
from schemas.user import User

from typing import Union


class TransactionController:
    # create transaction
    @staticmethod
    def create_transaction(
            card: Card,
            amount: float,
            timestamp: datetime.datetime,
            appr_status: bool) -> Account:
        transaction = Transaction(card_id=card.id, amount=amount, timestamp=timestamp, appr_status=appr_status)
        transaction.save()
        return transaction

    # read
    @staticmethod
    def get_transaction_by_id(id: int) -> Transaction:
        return Transaction.get(id=id)

    @staticmethod
    def get_approved_transactions_by_card(card: Card) -> [Transaction]:
        return Transaction.select().where(Transaction.card_id == card.id, Transaction.appr_status)

    # update
    @staticmethod
    def cancel_transaction_by_id(id: int) -> Transaction:
        transaction = TransactionController.get_transaction_by_id(id=id)
        transaction.appr_status = False
        transaction.save()
        print(f'Transaction with ID={id} was cancelled')
        return transaction

    # delete
    @staticmethod
    def delete_transaction(transaction: Transaction):
        transaction = TransactionController.get_transaction_by_id(id=transaction.id)
        transaction.delete_instance()
        print('Transaction deleted')
