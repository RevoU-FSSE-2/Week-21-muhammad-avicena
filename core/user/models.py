from dataclasses import dataclass

from core.user.constants import UserRole

@dataclass
class UserDomain:
    id: int
    username: str
    password: str
    role: UserRole
    bio: str