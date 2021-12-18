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
import urllib.request
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
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
        self.avgrating = avgrating


@app.route('/', methods=['POST', 'GET'])
def login():
    title = "Login"
    if request.method == 'POST':
        userid = request.form['userid']
        password = request.form['password']
        if userid == 'admin' and password == 'password':
            return redirect('/searchbook')
        else:
            return render_template("index.html", title=title)
    else:
        return render_template("index.html", title=title)


@app.route('/searchbook', methods=['POST', 'GET'])
def searchbook():
    title = "Searchbook"
    if request.method == 'POST':
        isbn = request.form['ISBN']
#        try:
        r = urllib.request.urlopen(f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}')
#            data = r.read()
        data = json.load(r)
        response = data["items"][0]["volumeInfo"]["title"]
        return render_template("searchbook.html", title=title, response=response)
#        except:
#            response = "That ISBN does not exist in our records. Try again."
#            return render_template("searchbook.html", title=title, response=response)
    else:
        return render_template("searchbook.html", title=title)


@app.route('/addbook', methods=['POST', 'GET'])
def addbook():
    title = "Addbook"
    if request.method == 'POST':
        title = "title"
        author = "author"
        pagecount = 1
        avgrating = 5
        newbook = Books(title=title, author=author, pagecount=pagecount, avgrating=avgrating)
        try:
            db.session.add(newbook)
            db.session.commit()
            return redirect('/searchbook')
        except:
            return "There was an error adding your book"
    else:
        return render_template("searchbook.html", title=title)


if __name__ == '__main__':
    db.init_app(app)
    db.create_all()
    app.run(debug=True)