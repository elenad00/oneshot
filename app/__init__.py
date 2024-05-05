from flask import Flask, render_template
import app.static.filler_text as filler_text

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True

@app.route('/')
def index() -> str:
    return render_template(
        'index.html',
        who_are_we=filler_text.who_are_we,
        membership = filler_text.membership
    )

@app.route('/user/<username>')
def profile(username: str) -> str:
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

@app.errorhandler(404)
def pnf(error):
    return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)