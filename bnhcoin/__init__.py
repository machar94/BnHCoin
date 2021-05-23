
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask_bcrypt import Bcrypt # hashing library
# from textwrap import dedent
# from uuid import uuid4

import bnhcoin.blockchain as blockchain


# Instantiate the blockchain
chain = blockchain.Blockchain();


# Instantiate our node
app = Flask(__name__);
app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'; # Set the database url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False;


# Setup database
db = SQLAlchemy(app);


# Object that facilitates hashing
bcrypt = Bcrypt(app);


# Setup login manager
loginManager = LoginManager(app);

# When a user attempts to access a login_required view without being
# logged in, it will redirect them to the login view
loginManager.login_view = 'login'; # login.html
loginManager.login_message_category = 'info';


from bnhcoin import db_user # Setup the user handler
from bnhcoin import routes # Setup the urls for the app


# # Generate a globally unique address for this node
# node_identifier = str(uuid4()).replace('-', '');
