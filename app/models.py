from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask.ext.login import UserMixin, AnonymousUserMixin
from flask import current_app
from . import mongo, login_manager

class Permission:
    FOLLOW = 0x01
    POST = 0x02
    MODERATE = 0x04
    ADMINISTER = 0x08

class Role:
    USER = Permission.FOLLOW |\
           Permission.POST
    MODERATOR = Permission.FOLLOW |\
                Permission.POST |\
                Permission.MODERATE
    ADMINISTRATOR = 0xff

class User(UserMixin):

    def __init__(self, username):
        self.username = username

    def get_id(self):
        return self.username

    def can(self, permissions):
        return self.role is not None and \
               (self.role & permissions) == permissions

    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    @property
    def role(self):
        doc = mongo.db.users.find_one({'_id': self.username},
                                      {'_id':0, 'role': 1})
        try:
            return doc['role']
        except KeyError, e:
            return None

    @role.setter
    def role(self, role):
        mongo.db.users.update_one({'_id': self.username},
                                  {'$set': { 'role': role}})

    @property
    def confirmed(self):
        doc = mongo.db.users.find_one({'_id': self.username},
                                      {'_id':0, 'confirmed': 1})
        try:
            return doc['confirmed']
        except KeyError, e:
            return False

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
    def add_user(username, email, password, role):
        mongo.db.users.insert_one({'_id': username, 'email': email,
                             'password_hash': generate_password_hash(password),
                             'role': role})

    @staticmethod
    def email_exists(email):
        user = mongo.db.users.find_one({'email': email})
        return True if user else False

    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)

    @staticmethod
    def generate_confirmation_token(username=None, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': username})

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


class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False
    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser

@login_manager.user_loader
def load_user(username):
    u = mongo.db.users.find_one({"_id": username})
    if not u:
        return None
    return User(u['_id'])