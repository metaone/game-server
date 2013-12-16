import motor
import bcrypt
from tornado import gen, web
from models.base import BaseModel


class UserModel(BaseModel):
    """User Model"""

    def __init__(self, db):
        BaseModel.__init__(self, db=db)

    @gen.engine
    def get_user_by_name(self, name, callback=None):
        user = yield motor.Op(self.db.users.find_one, {'username': name})
        callback(user)

    @gen.engine
    def register(self, username, email, password, callback=None):
        salt = bcrypt.gensalt()
        password_encode = password.encode('utf-8')
        password = bcrypt.hashpw(password_encode, salt)
        result = yield motor.Op(self.db.users.insert,
                                {'username': username, 'password': password, 'email': email, 'salt': salt})
        callback(result)

    @gen.engine
    def login(self, username, password, callback=None):
        result = False
        user = yield gen.Task(self.get_user_by_name, username)
        if user and user['password'] == bcrypt.hashpw(password.encode('utf-8'), user['salt'].encode('utf-8')):
            result = user
        callback(result)

        # user = self.db.users.find().sort([('username', 'admin'), ('password', 'admin')])

        # print cursor
        # for doc in (yield cursor.to_list()):
        #     print doc
        #
        # while (yield user.fetch_next):
        #     document = user.next_object()
        # print document
