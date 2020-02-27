from flask import Flask, request, redirect, url_for, session, render_template, make_response, jsonify
import queries
import os

app = Flask(__name__)

app.config[
    'SECRET_KEY'] = 'ojp[j3qj3iu-32u23utji23ht239ht-392ht8932-u-293u3189-u298-ut23-9th23-9t4389hjt8934-th9-23ht89-23htj2-938ht24-9ht24-t24-tj248t24=tj-24t'


@app.route('/', methods=['GET', 'POST'])
def home():
    if 'username' in session:
        return render_template('main_page.html', logged_in=session['username'], user_id=session['id'])
    else:
        return render_template('main_page.html', show_register='show')


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
        session['id'] = queries.return_user_id(username)
        return redirect(url_for('home'))
    elif queries.login_user(username, password) is False:
        return render_template('login_page.html', got_from='login', problem='wrong_cred')
    elif queries.login_user(username, password) is None:
        return render_template('login_page.html', got_from='login', problem='non_existent')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


@app.route('/print_users', methods=['GET', 'POST'])
def return_users():
    users = queries.return_users()
    print(users)


@app.route('/vote', methods=['POST'])
def vote():
    req = request.get_json()

    user_id = int(req['user_id'])
    planet_id = int(req['planet_id'])
    planet_name = req['planet_name']

    queries.add_vote(user_id, planet_id, planet_name)

    return make_response('OK', 200)


@app.route('/vote_stats')
def return_vote_stats():
    results = queries.vote_statistics()
    response = make_response(jsonify(results), 200)
    return response


if __name__ == '__main__':
    app.run(debug=True)
