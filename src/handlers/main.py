import tornado.websocket


class MainHandler(tornado.websocket.WebSocketHandler):
    """Main handler class"""

    connections = []

    def open(self):
        self.connections.append(self)

    def on_message(self, message):
        for connection in self.connections:
            connection.write_message(message)

    def on_close(self):
        self.connections.remove(self)
