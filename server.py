from flask import Flask, request, redirect, url_for, session, render_template
import queries
import os

app = Flask(__name__)

app.secret_key = os.urandom((20))


@app.route('/', methods=['GET', 'POST'])
def home():
    if 'username' in session:
        return render_template('main_page.html', logged_in=session['username'])
    else:
        return render_template('main_page.html', show_register = 'show')


@app.route('/login_page')
def return_login():
    return render_template('login_page.html', got_from='login', problem='no')


@app.route('/register_page')
def return_register():
    return render_template('login_page.html', got_from='register', problem='no')


@app.route('/register', methods=['GET', 'POST'])
def register():
    username = request.values.get('username')
    password = request.values.get('pass')

    if queries.add_user(username, password) is not False:
        return redirect(url_for('return_login'))
    else:
        return render_template('login_page.html', problem='user_exists', got_from='register')


@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.values.get('username')
    password = request.values.get('pass')

    if queries.login_user(username, password) is True:
        session['username'] = username
        return redirect(url_for('home'))
    else:
        return render_template('login_page.html', got_from='login', problem='wrong_cred')
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
