# Login
# List of books owned (title, author, page count, average rating)
# Add a book by searching Google Book API via ISBN
# https://www.googleapis.com/books/v1/volumes?q=isbn:9781449372620
# return appropriate error messages
# delete books from list
# EC: support multiple users (table with username, pass)
# EC: save links to thumbnails and display them
# EC:let user choose from multiple responses when adding a book
# EC: allow searching by title

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hw13.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(200), nullable=False)
    pagecount = db.Column(db.Integer, nullable=False)
    avgrating = db.Column(db.Integer, nullable=False)

    def __init__(self, title, author, pagecount, avgrating):
        self.title = title
        self.author = author
        self.pagecount = pagecount


@app.route('/', methods=['POST', 'GET'])
def login():
    title = "Login"
    if request.method == 'POST':
        userid = request.form['userid']
        password = request.form['password']
        if userid == 'admin' and password == 'password':
            return redirect('/dashboard')
        else:
            return render_template("index.html", title=title)
    else:
        return render_template("index.html", title=title)
