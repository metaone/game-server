import json
from handlers.base import BaseHandler
from tornado import gen
from models.user import UserModel


class LoginHandler(BaseHandler):
    """Login handler"""
    @gen.engine
    def on_message(self, message):
        result = {'valid': True, 'data': {'errors': [], 'fields': []}}
        data = json.loads(message)
        user = UserModel(self.settings['db'])
        login = yield gen.Task(user.login, data['username'], data['password'])

        if login:
            result['cookie'] = self.create_signed_value('user', data['username'])
        else:
            result['valid'] = False
            result['data']['fields'].append('username')
            result['data']['fields'].append('password')
            result['data']['errors'].append('invalid_credentials')

        self.write_message(json.dumps(result))
