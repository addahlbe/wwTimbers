from pyramid.view import (
    view_config,
    )
from pyramid.httpexceptions import (
    HTTPFound
)
from pyramid.security import NO_PERMISSION_REQUIRED
from wwtimbersApp.models import (
    User
)


@view_config(route_name='index', renderer='wwtimbersApp:templates/index.mako', permission=NO_PERMISSION_REQUIRED)
def index(request):
    return {}