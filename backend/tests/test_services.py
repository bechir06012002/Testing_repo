from app.services import apply_discount, authenticate, place_order, register_user


def test_register_user():
    user = register_user(1, "a@example.com")
    assert user.email == "a@example.com"


def test_authenticate():
    assert authenticate("secret", "secret") is True
    assert authenticate("wrong", "secret") is False


def test_place_order():
    order = place_order(user_id=1, amount_cents=1000)
    assert order.amount_cents == 1000


def test_apply_discount():
    assert apply_discount(1000, 10) == 900
