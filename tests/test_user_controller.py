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

def test_get_user_by_id():
    User.delete().execute()
    user_test = User(age=20, name='Alan')
    user_test.save()
    user_from_db = UserController.get_user_by_id(1)
    assert user_from_db.age == 20
    assert user_from_db.name == 'Alan'

def test_get_user_by_name():
    User.delete().execute()
    user_test = User(age=20, name='Alan')
    user_test.save()
    user_from_db = UserController.get_user_by_name('Alan')
    assert user_from_db.age == 20
    assert user_from_db.name == 'Alan'

def test_update_name():
    User.delete().execute()
    user_test = User(age=20, name='Alan')
    user_test.save()
    UserController.update_name(user_test, 'Aldo')
    user_from_db = User.get(name='Aldo')
    assert user_from_db.age == 20
    assert user_from_db.name == 'Aldo'