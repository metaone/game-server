#!/usr/bin/env python

import handlers.main as main
import handlers.auth as auth
import tornado.httpserver
import tornado.ioloop
import tornado.web
import motor
import conf.main as conf

application = tornado.web.Application(
    [
        (r'/ws', main.MainHandler),
        (r'/auth', auth.AuthHandler)
    ],
    db=motor.MotorClient().open_sync()[conf.settings['db_name']],
    cookie_secret=conf.settings['cookie_secret'],
    debug=conf.settings['debug_mode'])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(conf.settings['listen_port'])
    tornado.ioloop.IOLoop.instance().start()
