import json
import bcrypt
from validate_email import validate_email
from handlers.base import BaseHandler
from tornado import gen
from models.user import UserModel


class RegisterHandler(BaseHandler):
    """Register handler"""
    @gen.engine
    def on_message(self, message):
        data = json.loads(message)
        print data

        res = {
            'valid': True,
            'data': {
                'errors': [],
                'fields': []
            }
        }

        user = UserModel(self.settings['db'])

        if data['password'] != data['password_repeat']:
            res['valid'] = False
            res['data']['errors'].append('password_mismatch')
            res['data']['fields'].append('password')
            res['data']['fields'].append('password_repeat')

        if not validate_email(data['email']):
            res['valid'] = False
            res['data']['errors'].append('invalid_email')
            res['data']['fields'].append('email')

        user_exists = yield gen.Task(user.get_user_by_name, data['username'])
        if user_exists:
            res['valid'] = False
            res['data']['errors'].append('user_exists')
            res['data']['fields'].append('username')

        if res['valid']:
            insert = yield gen.Task(user.register,
                                    username=data['username'], email=data['email'], password=data['password'])

        self.write_message(json.dumps(res))
