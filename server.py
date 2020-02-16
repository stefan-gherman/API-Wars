from flask import Flask, request, redirect, url_for, session, render_template
import queries
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def home():

    return render_template('login_page.html')


@app.route('/login', methods =['GET', 'POST'])
def login():
    username = request.values.get('username')
    password = request.values.get('pass')

    if queries.add_user(username, password) is not False:
        return render_template('base.html')
    else:
        print('User already exists')
        return  None


if __name__ == '__main__':
    app.run(debug=True)
