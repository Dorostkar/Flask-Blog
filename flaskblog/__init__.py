from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '5cdcb08b231e45dcfe1be941de3b572a' #secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #these three slash means relative path.
db = SQLAlchemy(app)

from flaskblog import routes