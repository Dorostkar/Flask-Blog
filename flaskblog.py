from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5cdcb08b231e45dcfe1be941de3b572a' #secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #these three slash means relative path.
db = SQLAlchemy(app)

#simple database model for user
class User(db.Model):
    #because id is  primary_key it will be generated automatically
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    #backref : similar to adding new column to Post Model 
    #lazy: justify sqlAlchemy to load data as necessary in one go
    posts = db.relationship('Post',backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #the reasone of 'user' in foreignkey is lowercase is because we actually refrencing the table name and column name

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

"""
To create the data base:
1- open terminal and type python
2- from flaskblog import db
3- db.create_all()
then the .db file will created in the path
To add new data:
1- from flaskblog import User, Post
2- user_1 = User(username="Sina",email="sina@blog.com",password="password") : creating new user
3- db.session.add(user_1) : adding created user to db
4- db.session.commit(): commit our changes to database
Some queries with SQLAlchemy:
User.query.all() :will run __repr__ per each user
User.query.first()
User.query.filter_by(username='Sina').all()
User.query.filter_by(username='Sina').first()
can be assigned to a variable:
user=User.query.filter_by(username='Sina').first()
user.id
user.username
Get user by Id:
user = User.query.get(1) : 1 is an id
post_1 = Post(title="Blog 1",content="First Post Content" ,user_id = user.id)
db.session.add(post_1)
db.session.commit()

Get Author from post:
post.author => will return: User('Sina', 'sina@blog.com', 'default.jpg')

delete tables:
db.drop_all()

"""

posts=[
    {
        'author':'Sina Dorostkar',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'April 20,2018'
    },
     {
        'author':'Sina Dorostkar',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'April 21,2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title='About')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
           flash('You have been logged in!', 'success') 
           return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password','danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)