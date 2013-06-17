#!/usr/bin/env python

import handlers.main
import tornado.httpserver
import tornado.ioloop
import tornado.web


application = tornado.web.Application([
    (r'/ws', handlers.main.MainHandler),
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
