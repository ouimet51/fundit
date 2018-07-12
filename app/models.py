from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

#Defines Table for Users
class User(UserMixin, db.Model):

	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(120), index=True)
	lastname = db.Column(db.String(120), index=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	account = db.Column(db.Integer, default=0)
	funds = db.relationship('Fund', backref='creator', lazy='dynamic')
	contributions = db.relationship('Contribution', backref='contributor', lazy='dynamic')
	transfers = db.relationship('Transfer', backref='transactor', lazy='dynamic')

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return '<User {}>'.format(self.email)

@login.user_loader
def load_user(id):
	return User.query.get(int(id))

# Defines table for Funds(goals)
class Fund(db.Model):
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120), index=True)
	description = db.Column(db.String(140))
	goal = db.Column(db.Integer)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	contribution = db.relationship('Contribution', backref='fund', lazy='dynamic')

	def __repr__(self):
		return '<Fund {}>'.format(self.name)

#Defines table for contributions, a user can contibute to a fund
class Contribution(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	value = db.Column(db.Integer)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	fund_id = db.Column(db.Integer, db.ForeignKey('fund.id'))

	def __repr__(self):
		return '<Contribution {}>'.format(self.value)

#Defines table for transfers. A user can transfer value to their account
class Transfer(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	value = db.Column(db.Integer)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Transfer {}>'.format(self.value)





