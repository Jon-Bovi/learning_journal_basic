"""Define view handlers."""
from pyramid.view import view_config
from .entries import get_entries, ENTRIES
from datetime import date
import pyramid.httpexceptions as exc
import os


THIS_DIR = os.path.dirname(__file__)
ENTRIES_DICT = get_entries()


@view_config(route_name="home", renderer="templates/home.jinja2")
def home(request):
    """Home view handler."""
    # file_data = open(os.path.join(THIS_DIR, 'templates/index.html')).read()
    return ENTRIES_DICT


@view_config(route_name="detail", renderer="templates/detail.jinja2")
def detail(request):
    """Detail view handler."""
    idx = len(ENTRIES) - int(request.matchdict['id'])
    if idx > 0:
        return ENTRIES[len(ENTRIES) - int(request.matchdict['id'])]
    raise exc.HTTPNotFound()


@view_config(route_name="update", renderer="templates/update.jinja2")
def update(request):
    """Update/edit view handler."""
    idx = len(ENTRIES) - int(request.matchdict['id'])
    if idx > 0:
        return ENTRIES[len(ENTRIES) - int(request.matchdict['id'])]
    raise exc.HTTPNotFound()


@view_config(route_name="create", renderer="templates/create.jinja2")
def create(request):
    """Create new view handler."""
    today = date.today()
    return {"date": "{}-{}-{}".format(today.year, today.month, today.day)}
