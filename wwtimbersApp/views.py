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


@view_config(route_name='history', renderer='wwtimbersApp:templates/history.mako', permission=NO_PERMISSION_REQUIRED)
def history(request):
    return {}


@view_config(route_name='glu-lam/decking', renderer='wwtimbersApp:templates/decking.mako', permission=NO_PERMISSION_REQUIRED)
def decking(request):
    return {}


@view_config(route_name='solid-timbers', renderer='wwtimbersApp:templates/timbers.mako', permission=NO_PERMISSION_REQUIRED)
def timbers(request):
    return {}


@view_config(route_name='outdoor-structures', renderer='wwtimbersApp:templates/structures.mako', permission=NO_PERMISSION_REQUIRED)
def structures(request):
    return {}


@view_config(route_name='crane-pads', renderer='wwtimbersApp:templates/crane.mako', permission=NO_PERMISSION_REQUIRED)
def crane(request):
    return {}


@view_config(route_name='repair-work', renderer='wwtimbersApp:templates/repair.mako', permission=NO_PERMISSION_REQUIRED)
def repair(request):
    return {}


@view_config(route_name='brochure', renderer='wwtimbersApp:templates/brochure.mako', permission=NO_PERMISSION_REQUIRED)
def brochure(request):
    return {}


@view_config(route_name='contact-us', renderer='wwtimbersApp:templates/contact.mako', permission=NO_PERMISSION_REQUIRED)
def contact(request):
    return {}
