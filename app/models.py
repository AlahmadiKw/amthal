from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask.ext.login import UserMixin
from flask import current_app
from . import mongo, login_manager


class User(UserMixin):

    def __init__(self, username):
        self.username = username

    def get_id(self):
        return self.username

    def confirmed(self):
        doc = mongo.db.users.find_one({'_id': self.username},
                                      {'_id':0, 'confirmed': 1})
        try:
            return doc['confirmed']
        except KeyError, e:
            return False

    def generate_confirmation_token(self, expiration=3600):
        print self.username
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.username})

    @property
    def email(self):
        doc = mongo.db.users.find_one({'_id': self.username},
                                      {'_id':0, 'email': 1})
        try:
            return doc['email']
        except KeyError, e:
            return False

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

    @staticmethod
    def confirm(username, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != username:
            return False
        mongo.db.users.update_one({'_id': username},
                                  {'$set': { 'confirmed': True}})
        return True


@login_manager.user_loader
def load_user(username):
    u = mongo.db.users.find_one({"_id": username})
    if not u:
        return None
    return User(u['_id'])