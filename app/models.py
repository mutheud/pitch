from .import db
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model):

    __tablename__ = 'users'
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot access password')

    password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password)


    # role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return f'user {self.username}'

# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer,primary_key = True)
#     username = db.Column(db.String(255))

#     def __repr__(self):
#         return f'users {self.username}'