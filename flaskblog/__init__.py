import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# pip install flask-bcrypt
from flask_bcrypt import Bcrypt
#pip install flask-login
from flask_login import LoginManager #for creating login system.
from flask_mail import Mail
app = Flask(__name__)
app.config['SECRET_KEY'] = '5cdcb08b231e45dcfe1be941de3b572a' #secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #these three slash means relative path.
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)



from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)