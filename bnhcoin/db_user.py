from bnhcoin import db, loginManager
from flask_login import UserMixin


@loginManager.user_loader
def loadUser(user_id):
	return User.query.get(int(user_id));

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(35), unique = False, nullable=False);
    username = db.Column(db.String(15), unique = True, nullable=False);
    password = db.Column(db.String(120), unique = False, nullable=False);

    def __repr__(self):
        return f"User('{self.name}', '{self.username}')";
