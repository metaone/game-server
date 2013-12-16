#!/usr/bin/env python

from handlers.main import MainHandler
from handlers.login import LoginHandler
from handlers.register import RegisterHandler

import tornado.httpserver
import tornado.ioloop
import tornado.web
import motor
import conf.main as conf

application = tornado.web.Application(
    [
        (r'/ws', MainHandler),
        (r'/login', LoginHandler),
        (r'/register', RegisterHandler),
    ],
    db=motor.MotorClient().open_sync()[conf.settings['db_name']],
    cookie_secret=conf.settings['cookie_secret'],
    debug=conf.settings['debug_mode'])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(conf.settings['listen_port'])
    tornado.ioloop.IOLoop.instance().start()
