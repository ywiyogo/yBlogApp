import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'

COLORS = ['#707281', # grey
          '#E67E22', #orange
          '#47bac9', # turkies
          '#564d52',
          '#68c02e',
          '#1abc9c']


app = Flask(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)


@app.route("/")
def home():
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    posts.sort(key=lambda item: item['date'], reverse=False)

    # adding background color to post metadata
    ind = 0
    for post in posts:
        post.meta['bgcolor'] = COLORS[ind]
        ind = ind + 1
        if ind == len(COLORS):
            ind = 0

    return render_template('index.html', posts=posts)


@app.route("/resume/")
def resume():
    return render_template('resume.html')


@app.route("/contact/")
def contact():
    return render_template('contact.html')


@app.route("/posts/")
def posts():
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    posts.sort(key=lambda item: item['date'], reverse=False)
    return render_template('posts.html', posts=posts)


@app.route('/posts/<name>/')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)


@app.route("/fragmentor")
def fragmentor():
    return render_template('fragmentor.html')


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', port=8000, debug=True)
