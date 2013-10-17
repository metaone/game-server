#!/usr/bin/env python

import handlers.main as main
import handlers.auth as auth
import tornado.httpserver
import tornado.ioloop
import tornado.web
import motor


application = tornado.web.Application(
    [
        (r'/ws', main.MainHandler),
        (r'/auth', auth.AuthHandler)
    ],
    db=motor.MotorClient().open_sync().game,
    cookie_secret="jBRGCR1SB7k7oa2Mii8f",
    debug=True)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
