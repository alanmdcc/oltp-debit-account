from controllers.account_controller import AccountController
from schemas.user import User


class UserController:
    # create user
    @staticmethod
    def create_user(age: int, name: str) -> User:
        user = User(age=age, name=name)
        user.save()
        return user

    # read
    @staticmethod
    def get_user_by_id(id: int):
        return User.get(id=id)

    @staticmethod
    def get_user_by_name(name: str) -> User:
        return User.get(name=name)

    # update
    @staticmethod
    def update_name(user: User, name: str):
        user.name = name
        user.save()
        print(f'Name updated for user ID={User.id}')
        return user

    # delete
    @staticmethod
    def delete_user(user: User):
        try:
            account = user.get(user_id=user.id)
        except:
            account = None

        if account is None:
            print(f'User with ID={user.id} was deleted')
            user.delete_instance()
        else:
            print(f'User with ID={user.id} and account with ID={account.id} was deleted')
            AccountController.delete_account(account=account)
            user.delete_instance()
