from dataclasses import dataclass, field


@dataclass
class User:
    id: int
    email: str
    is_admin: bool = False
    tags: list[str] = field(default_factory=list)
