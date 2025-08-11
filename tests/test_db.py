from fastapi_zero.models import User


# TODO Continuar aula 04 no minuto 46:20 https://www.youtube.com/watch?v=I7IrmN7jMqE
def test_create_user(session):
    user = User(
        username='Bob',
        email='bob@example.com',
        password='secret',
    )

    session.add(user)
    session.commit()

    assert user.username == 'Bob'
    assert user.email == 'bob@example.com'
