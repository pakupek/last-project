from flask import render_template
from blog import app
from blog.models import Entry


#Route leading into homepage
@app.route('/')
def homepage():
    all_posts = Entry.query.all()
    return render_template('homepage.html', all_posts_=all_posts)
