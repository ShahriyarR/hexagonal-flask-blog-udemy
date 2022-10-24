from flask import Flask

from src.main.containers import Container
from src.main.config import init_app


def create_app() -> Flask:
  container = Container()
  app = Flask(__name__)
  app.secret_key = "Awesome Secret Key which is going to be hacked."
  app.container = container
  with app.app_context():
    init_app(app)
  app.add_url_rule("/", endpoint="index")
  return app