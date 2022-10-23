from .repository import RepositoryInterface
from . import RegisterUserInputDto, UserOutputDto
from ..model import user_factory
from typing import Optional


class UserDBOperationError(Exception):
    ...


class UserService:

    def __init__(self, user_repo: RepositoryInterface) -> None:
        self.user_repo = user_repo


    def create(self, user: RegisterUserInputDto) -> Optional[UserOutputDto]:
      user = user_factory(user_name=user.user_name, password=user.password)
      data = (user.uuid, user.user_name, user.password)
      query = "INSERT INTO user (uuid, username, password) VALUES (?, ?, ?)"
      try:
        self.user_repo.execute(query, data, commit=True)
      except Exception as err:
        raise UserDBOperationError(err) from err
      finally:
        user = self.get_user_by_user_name(user.user_name)
      return user

    def get_user_by_user_name(self, user_name: str) -> Optional[UserOutputDto]:
      data = (user_name, )
      query = "SELECT * FROM user WHERE username = ?"
      try:
        user = self.user_repo.execute(query, data).fetchone()
      except Exception as err:
        raise UserDBOperationError() from err
      finally:
        user = UserOutputDto(id=user["id"], uuid=user["uuid"], user_name=user["username"])
      return user
        

    def get_user_by_id(self, id_: int) -> Optional[UserOutputDto]:
      data = (id_,)
      query = "SELECT * FROM user WHERE id = ?"
      try:
        user = self.user_repo.execute(query, data).fetchone()
      except Exception as err:
        raise UserDBOperationError() from err
      finally:
        user = UserOutputDto(id=user["id"], uuid=user["uuid"], user_name=user["username"])
      return user
        