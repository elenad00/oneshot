from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index() -> str:
    return render_template('home.html')

@app.route('/<username>')
def profile(username) -> str:
    return render_template('profile.html')

@app.route('/write')
def books():
    return render_template('write.html')


# basic log in sign up functions
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/error')
def error():
  return render_template('blank.html')


if __name__ == '__main__':
    app.run(debug=True)