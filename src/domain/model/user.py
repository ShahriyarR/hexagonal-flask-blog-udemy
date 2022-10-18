import uuid
from dataclasses import dataclass

@dataclass
class User:
  uuid: str
  user_name: str
  password: str


def user_factory(user_name: str, password: str) -> User:
  return User(uuid=str(uuid.uuid4()), user_name=user_name, password=password)