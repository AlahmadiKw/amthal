from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from . import mongo, login_manager


class User(UserMixin):

    def __init__(self, username):
        self.username = username

    def get_id(self):
        return self.username

    @staticmethod
    def get_user(username):
        user = mongo.db.users.find_one({'_id': username})
        return user if user else None

    @staticmethod
    def add_user(username, email, password):
        mongo.db.users.insert_one({'_id': username, 'email': email,
                             'password_hash': generate_password_hash(password)})

    @staticmethod
    def email_exists(email):
        user = mongo.db.users.find_one({'email': email})
        return True if user else False

    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)


@login_manager.user_loader
def load_user(username):
    u = mongo.db.users.find_one({"_id": username})
    if not u:
        return None
    return User(u['_id'])