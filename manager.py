import os

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

from cookie.app import create_app
from cookie.settings import config


env = 'prod' if os.environ.get('TORNADO_ENV') == 'production' else 'dev'
app = create_app(config=config[env])
define('port', default=8000, help='run on the given port', type=int)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
