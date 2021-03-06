from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from wwtimbersApp.models import initialize_base
from pyramid.session import UnencryptedCookieSessionFactoryConfig


def get_db(request):
    maker = request.registry.settings['db.sessionmaker']
    return maker()


def main(global_config, **settings):
    '''Main config function'''

    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_base(engine)
    maker = sessionmaker(bind=engine)
    settings['db.sessionmaker'] = maker

    my_session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
    config = Configurator(settings=settings,
                          session_factory=my_session_factory)

    config.set_request_property(get_db, 'db', reify=True)

    #Static routes
    config.add_static_view('style', 'wwtimbersApp:dependencies/')

    # Routes
    # HOME
    config.add_route('index', '/')
    config.add_route('history', '/history')
    config.add_route('decking', '/decking')
    config.add_route('solid-timbers', '/solid-timbers')
    config.add_route('outdoor-structures', '/outdoor-structures')
    config.add_route('crane-pads', '/crane-pads')
    config.add_route('repair-work', '/repair-work')
    config.add_route('brochure', '/brochure')
    config.add_route('contact-us', '/contact-us')

    config.scan('wwtimbersApp')
    return config.make_wsgi_app()
