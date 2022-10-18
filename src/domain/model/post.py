import uuid
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Post:
  uuid: str
  author_id: int
  title: str
  body: str
  created: datetime


def post_factory(author_id: int, title: str, body: str, created=None) -> Post:
  # proper data validation or type validation should happen here
  _created = created or datetime.now()
  return Post(uuid=str(uuid.uuid4()), author_id=author_id, 
              title=title, body=body, created=_created)