#!/usr/bin/env python

import handlers.main
import handlers.auth as auth
import tornado.httpserver
import tornado.ioloop
import tornado.web


application = tornado.web.Application([
    (r'/ws', handlers.main.MainHandler),
    (r'/auth', auth.AuthHandler)
], cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__")

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
