# -*- coding:utf-8 -*-


# import os.path

from tornado import httpserver
from tornado import ioloop
from tornado import web

class TestHandler(web.RequestHandler):
    def get(self):
        self.write("Hello, World!")

def main():
    settings = {
        # "static_path": os.path.join(os.path.dirname(__file__), "static"),
    }
    application = web.Application([
        (r"/", TestHandler),
    ], **settings)
    server = httpserver.HTTPServer(application,
           #                         ssl_options={
           # "certfile": os.path.join(os.path.abspath("."), "server.crt"),
           # "keyfile": os.path.join(os.path.abspath("."), "server.key"),
    # }
    )
    server.listen(8000)
    ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
