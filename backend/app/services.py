from app.models import Order, User

_USERS: dict[int, User] = {}
_ORDERS: dict[int, Order] = {}


def authenticate(api_key: str, expected_key: str) -> bool:
    return api_key == expected_key


def place_order(user_id: int, amount_cents: int) -> Order:
    order_id = len(_ORDERS) + 1
    order = Order(id=order_id, user_id=user_id, amount_cents=amount_cents)
    _ORDERS[order_id] = order
    return order


def apply_discount(amount_cents: int, percent: int) -> int:
    return amount_cents - (amount_cents * percent // 100)


def get_user_orders(user_id: int) -> list[Order]:
    return [o for o in _ORDERS.values() if o.user_id == user_id]
