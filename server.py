from flask import Flask, request, redirect, url_for, session, render_template
from psycopg2 import sql
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login_page.html')



if __name__ == '__main__':
    app.run(debug=True)
