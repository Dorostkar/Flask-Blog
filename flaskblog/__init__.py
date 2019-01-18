from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# pip install flask-bcrypt
from flask_bcrypt import Bcrypt
#pip install flask-login
from flask_login import LoginManager #for creating login system.
app = Flask(__name__)
app.config['SECRET_KEY'] = '5cdcb08b231e45dcfe1be941de3b572a' #secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #these three slash means relative path.
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes