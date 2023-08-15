from datetime import date

from controllers.account_controller import AccountController
from schemas.account import Account
from schemas.user import User


def test_create_account():
    User.delete().execute()
    Account.delete().execute()
    user_test = User(age=20, name='Alan')
    user_test.save()
    account_test = AccountController.create_account(user=user_test,balance=1000,open_date='2021-01-01')
    assert account_test.balance == 1000
    assert account_test.open_date == '2021-01-01'

def test_get_account_by_user():
    User.delete().execute()
    Account.delete().execute()
    user_test = User(age=20, name='Alan')
    user_test.save()
    account_test = Account(user_id=user_test.id,balance=1000,open_date='2021-01-01' )
    account_test.save()
    account_from_db = AccountController.get_account_by_user(user_test)
    assert account_from_db.balance == 1000
    assert account_from_db.open_date ==  date(2021,1,1)
