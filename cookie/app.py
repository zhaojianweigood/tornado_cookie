import tornado.web


def create_app(config):
    handlers = register_handlers()
    app = tornado.web.Application(handlers=handlers, settings=config)
    register_extensions(app)
    return app


def register_handlers():
    from cookie.urls import urlpatterns
    return urlpatterns


def register_extensions(app):
    pass
