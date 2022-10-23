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