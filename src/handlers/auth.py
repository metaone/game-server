import json
import tornado.gen
import tornado.websocket
import tornado.web
from tools.auth import Auth


class AuthHandler(tornado.websocket.WebSocketHandler):
    """Auth handler class"""
    def open(self):
        pass

    @tornado.gen.coroutine
    def on_message(self, message):
        data = json.loads(message)
        print data

        cursor = self.settings['db'].users.find()
        # print cursor
        # for doc in (yield cursor.to_list()):
        #     print doc

        while (yield cursor.fetch_next):
            document = cursor.next_object()
            print document

        # print self.settings['db'].users

        cookie = self.create_signed_value('user', data['username'])
        # print cookie
        # print tornado.web.decode_signed_value(self.application.settings["cookie_secret"], 'user', cookie)

        auth = Auth()

        if auth.login(data['username'], data['password']):
            self.write_message(json.dumps({
                'status': 'success',
                'cookie': cookie
            }))
        else:
            self.write_message(json.dumps({
                'status': 'error'
            }))

    def on_close(self):
        pass
