from dataclasses import dataclass, asdict


@dataclass
class RegisterUserInputDto:
    user_name: str
    password: str

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)


@dataclass
class UserOutputDto:
  id: int
  uuid: str
  user_name: str

  def to_dict(self):
    return asdict(self)

  @classmethod
  def from_dict(cls, dict_):
      return cls(**dict_)


@dataclass
class CreatePostInputDto:
    title: str
    body: str
    author_id: int

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)


def create_post_factory(title: str, body: str, author_id: int) -> CreatePostInputDto:
    return CreatePostInputDto(title=title, body=body, author_id=author_id)


@dataclass
class UpdatePostInputDto:
    id: int
    title: str
    body: str

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)


def update_post_factory(id: int, title: str, body: str) -> UpdatePostInputDto:
    return UpdatePostInputDto(id=id, title=title, body=body)


@dataclass
class DeletePostInputDto:
    id: int

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)


def delete_post_factory(id: int) -> DeletePostInputDto:
    return DeletePostInputDto(id=id)