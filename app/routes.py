from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
  user = { 'username' : 'Raja'}
  posts = [
    {
      'author' : {'username': 'John'},
      'body' : 'Beatiful day in Portland!'
    }

,    {
      'author' : { 'username' : "Dippa"},
      'body' : 'The Avengers movie is so cool!'
    }

  ]
  return render_template('index.html', title="Home", user=user, posts=posts)