import tornado.websocket
import tornado.web
import json


class AuthHandler(tornado.websocket.WebSocketHandler):
    """Auth handler class"""

    def open(self):
        pass

    def on_message(self, message):
        # self.get_secure_cookie()

        # self.set_secure_cookie()

        data = json.loads(message)
        print data
        cookie = self.create_signed_value('user', 'test')
        print cookie
        print tornado.web.decode_signed_value(self.application.settings["cookie_secret"], 'user', cookie)

        if data['username'] == 'admin' and data['password'] == 'admin':
            self.write_message(json.dumps({
                'status' : 'success',
                'cookie' : cookie
            }))
        else:
            self.write_message(json.dumps({
                'status' : 'error'
            }))

    def on_close(self):
        pass
