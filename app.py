from flask import Flask, render_template


app = Flask(__name__)


##test
@app.route('/user/<username>')
def shouw_user_profile(username):
    return 'User:  {}!!'.format(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath: {}'.format(subpath)


@app.route('/login')
def login():
    return render_template('index.html')


@app.route('/logout')
def logout():
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('index.html')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
