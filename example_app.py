"""Our single page Tweepy web application"""
from os import getenv
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from twitter import get_info

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
DB = SQLAlchemy(app)


# endpoint == "/"
@app.route("/")
def root():
    users = User.query.all()
    return render_template("base.html", users=users)


# endpoint == "user_submitted"
@app.route("/user_submitted", methods=["POST"])
def user_submitted():
    username = request.values["username"]
    # dtypes: user = <user twitter object>, user_tweets = <tweets list>
    user, user_tweets = get_info(username)
    DB_user = User(
        id=user.id,
        username=user.name,
        fullname=user.name,
        tweets=user_tweets
    )
    DB.session.add(DB_user)
    DB.session.commit()
    return render_template("user.html", username=username, tweets=user_tweets)


# endpoint == "reset"
@app.route("/reset")
def reset():
    DB.drop_all()
    DB.create_all()
    return render_template("reset.html")


# Creating a user database
class User(DB.Model):
    """Stores Twitter users and corresponding tweets"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    username = DB.Column(DB.String(50), nullable=False)
    fullname = DB.Column(DB.String(50), nullable=False)
    tweets = DB.Column(DB.PickleType)

    def __repr__(self):
        return "<User {}>".format(self.fullname)
