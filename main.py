import datetime

from controllers.account_controller import AccountController
from controllers.card_controller import CardController
from controllers.user_controller import UserController
from db.migrations import create_db

from schemas.account import Account
from schemas.card import Card
from schemas.transaction import Transaction
from schemas.user import User

if __name__ == '__main__':
    create_db('./db/db_oltp.db')

    user = UserController.create_user(age=43, name='Tomas Campos')

    account = AccountController.create_account(user=user, balance=3000, open_date=datetime.datetime.now())

    card1 = CardController.create_card(account=account, name='Gold', cvv='321')

    print('Make a deposit of 1000')
    AccountController.deposit(account, 1000)

    print('Make a withdraw of 1500')
    AccountController.withdraw(account, 1500)

    print('Account created:')
    for i in Account.select():
        print(f'ID={i.id}, User ID={i.user_id}, Balance={i.balance}, Open Date={i.open_date}')

    print('User created:')
    for i in User.select():
        print(f'ID={i.id}, Age={i.age}, Name={i.name}')

    print('Card created:')
    for i in Card.select():
        print(f'ID={i.id}, Account ID={i.account_id}, Name={i.name}, CVV={i.cvv}')

    print('Transactions made:')
    for i in Transaction.select():
        print(f'ID={i.id}, Amount={i.amount}, Creation timestamp={i.timestamp}, Approved={i.appr_status}')
