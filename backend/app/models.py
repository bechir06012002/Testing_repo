from dataclasses import dataclass, field


@dataclass
class User:
    id: int
    email: str
    is_admin: bool = False
    tags: list[str] = field(default_factory=list)


@dataclass
class Order:
    id: int
    user_id: int
    amount_cents: int
    status: str = "pending"
