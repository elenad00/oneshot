from flask import render_template, redirect, url_for
from writeaway import app
import writeaway.static.scripts.filler_text as filler_text
import writeaway.static.scripts.user_configs as user_configs
import writeaway.static.scripts.user_statistics as user_statistics

@app.route('/')
def index() -> render_template:
    if user_configs.logged_in():
        return redirect(url_for('home'))
    else:
        return render_template(
            'index.html',
            who_are_we=filler_text.who_are_we,
            membership = filler_text.membership
        )
    
@app.route('/home')
def home() -> render_template:
    publisher_count, editor_count = user_statistics.get_interest()
    user_portfolio = user_statistics.get_user_portfolio()
    return render_template(
        'home.html', 
        username=user_configs.get_username(),
        publisher_count=publisher_count, 
        editor_count=editor_count,
        user_portfolio=user_portfolio
    )

@app.route('/user/<username>')
def profile(username: str) -> render_template:
    return render_template(
        'profile.html',
        username=username
    )

@app.route('/write')
def books() -> render_template:
    return render_template('write.html')

# basic log in sign up functions
@app.route('/login')
def login() -> render_template:
    return render_template('login.html')

@app.route('/signup')
def signup() -> render_template:
    return render_template('signup.html')

@app.route('/about_us')
def about_us() -> render_template:
    return render_template(
        'about_us.html',
        who_are_we=filler_text.who_are_we,
        membership = filler_text.membership
    )

@app.errorhandler(404)
def pnf(error) -> render_template:
    return render_template('error.html')
