from .import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):

    __tablename__ = 'users'
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index =True)
    email = db.Column(db.String(255),unique = True,index = True)
    # role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('Pitch',backref = 'user', lazy = 'dynamic')
    comments = db.relationship('Comment',backref = 'user',lazy ='dynamic')
 

    @property
    def password(self):
        raise AttributeError('You cannot access password')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

          
    
    def __repr__(self):
        return f'user {self.username}'


class Pitch(db.Model):
    __tablename__ = 'pitch'
    
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    pitch =db.Column(db.String(255),index = True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comment',backref = 'pitch', lazy ='dynamic')
    category = db.Column(db.String(255))
    # bio = db.relationship('users',backref = 'pitch',lazy = 'dynamic')
    
    
class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    comment =db.Column(db.String(255),index = True)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

