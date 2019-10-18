import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('getting', 'Hello')
        self.write(greeting + 'world')
