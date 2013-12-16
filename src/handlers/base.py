import tornado.gen
import tornado.websocket


class BaseHandler(tornado.websocket.WebSocketHandler):
    """Base handler"""

    connections = []

    @tornado.gen.coroutine
    def open(self):
        pass

    @tornado.gen.coroutine
    def on_message(self, message):
        pass

    @tornado.gen.coroutine
    def on_close(self):
        pass
