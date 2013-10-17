import tornado.websocket


class BaseHandler(tornado.websocket.WebSocketHandler):
    """Main handler class"""

    connections = []

    def open(self):
        pass

    def on_message(self, message):
        pass

    def on_close(self):
        pass
