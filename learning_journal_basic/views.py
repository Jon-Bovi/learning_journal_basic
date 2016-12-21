from pyramid.view import view_config
import os


THIS_DIR = os.path.dirname(__file__)


@view_config(route_name="home", renderer="templates/list.jinja2")
def home(request):
    """Home view handler."""
    # file_data = open(os.path.join(THIS_DIR, 'templates/index.html')).read()
    stuff = [
        'orange',
        'pen',
        'knife',
    ]
    return {"bag": stuff}


@view_config(route_name="detail", renderer="string")
def detail(request):
    """Detail view handler."""
    file_data = open(os.path.join(THIS_DIR, 'data/detail.html')).read()
    return file_data


@view_config(route_name="update", renderer="string")
def update(request):
    """Update/edit view handler."""
    file_data = open(os.path.join(THIS_DIR, 'templates/update.html')).read()
    return file_data


@view_config(route_name="create", renderer="string")
def create(request):
    """Create new view handler."""
    file_data = open(os.path.join(THIS_DIR, 'templates/create.html')).read()
    return file_data


# def includeme(config):
#     """Pyramid view configuration."""
#     config.add_view(home, route_name="home")
#     config.add_view(detail, route_name="detail")
#     config.add_view(update, route_name="update")
#     config.add_view(create, route_name="create")
