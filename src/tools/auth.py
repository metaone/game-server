import tornado.web
import motor


class Auth(object):
    def login(self, username=None, password=None):

        # db = self.settings['db']

        # print db

        if username == 'admin' and password == 'admin':
            return True
        else:
            return False
