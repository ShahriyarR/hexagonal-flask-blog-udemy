from Flask import Blueprint, request, redirect, render_template, url_for, flash
from src.domain.ports.user_service import UserService, UserDBOperationError
from dependency_injector.wiring import inject, Provide
from src.main.containers import Container
from src.domain.ports import register_user_factory


blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@blueprint.route('/register', methods=('GET', 'POST'))
@inject
def register(user_service: UserService = Provide[Container.user_package.user_service]):
  if request.method == 'POST':
    user_name = request.form['username']
    password = request.form['password']
    error = None
    if not user_name:
        error = 'Username is required.'
    elif not password:
        error = 'Password is required.'

    user_ = register_user_factory(user_name=user_name, password=password)
    if user_:
      try:
        user_service.create(user_)
      except UserDBOperationError as err:
        print(err)
        error = f"Something went wrong with database operation {err}"
      else:
        return redirect(url_for("auth.login"))
    flash(error)

  return render_template('auth/register.html')


    