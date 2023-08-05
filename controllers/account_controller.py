import datetime

from schemas.account import Account
from schemas.card import Card
from schemas.user import User

from typing import Union


class AccountController:
    # create account
    @staticmethod
    def create_account(
            user: User,
            balance: float,
            open_date: datetime.datetime) -> Account:
        account = Account(user_id=user.id, balance=balance, open_date=open_date)
        account.save()
        return account

    # read
    @staticmethod
    def get_account_by_id(id: int) -> Account:
        return Account.get(id=id)

    @staticmethod
    def get_account_by_user(user: User) -> Union[Account, None]:
        try:
            return Account.get(user_id=user.id)
        except Account.DoesNotExist:
            return None

    @staticmethod
    def get_account_by_card(card: Card) -> Account:
        return Account.get(id=card.account_id)

    # update
    @staticmethod
    def deposit(account, amount) -> bool:
        balance = account.balance + amount
        account.balance = balance
        account.save()
        print('Deposit completed')
        print(f'Updated balance: {account.balance}')
        return True

    @staticmethod
    def withdraw(account, amount) -> bool:
        balance = account.balance - amount
        if balance >= 0:
            account.balance = balance
            account.save()
            print('Withdraw completed')
            print(f'Updated balance: {account.balance}')
            return True
        else:
            print('Not enough balance to complete the transaction')
            print(f'Current balance: {account.balance}')
            return False

    # delete
    @staticmethod
    def delete_account(account: Account):
        try:
            card = Account.get(account_id=account.id)
        except:
            card = None

        if card is None:
            print(f'Account with ID={account.id} was deleted')
            account.delete_instance()
        else:
            print(f'Account with ID={account.id} and card with ID={card.id} was deleted')
            card.delete_instance()
            account.delete_instance()
