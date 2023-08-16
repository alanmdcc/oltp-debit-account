from controllers.user_controller import UserController
from schemas.user import User


def test_create_user():
    User.delete().where(User.name == 'Alan')
    user_test = UserController.create_user(age=20, name='Alan')
    assert user_test.age == 20
    assert user_test.name == 'Alan'

    user_test_from_db = User.get(name='Alan')
    print(user_test_from_db)
    assert user_test_from_db.age == 20
    assert user_test_from_db.name == 'Alan'
