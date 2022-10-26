from flask import Blueprint, render_template, request, flash, g, redirect, url_for
from dependency_injector.wiring import inject, Provide
from src.adapters.app.blueprints.auth import login_required
from src.domain.ports.post_service import PostService, BlogDBOperationError
from src.domain.ports import create_post_factory
from src.main.containers import Container

blueprint = Blueprint('post', __name__)


@blueprint.route('/create', methods=('GET', 'POST'))
@login_required
@inject
def create(post_service: PostService = Provide[Container.blog_package.post_service]):
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        post = create_post_factory(author_id=g.user["id"], title=title, body=body)
        if not error:
            try:
                post_service.create(post)
            except BlogDBOperationError as err:
                error = f"Something went wrong with database operation {err}"
            else:
                return redirect(url_for('post.index'))
        flash(error)

    return render_template('post/create.html')