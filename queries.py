from psycopg2 import sql
import psycopg2

import utils

import db_connection


@db_connection.connection_handler
def add_user(cursor, username, password):
    cursor.execute(
        sql.SQL("SELECT {col1} from {table} WHERE {col1} = (%s);")
            .format(
            col1=sql.Identifier('username'),
            table=sql.Identifier('userbase'),
        ), [username]
    )

    user_exist = cursor.fetchall()

    if len(user_exist) == 0:
        hashed_pw = utils.hash_password(password)
        cursor.execute(
            sql.SQL("INSERT INTO {userbase} ({usrnam}, {password}) VALUES (%s, %s);")
                .format(
                userbase=sql.Identifier('userbase'),
                usrnam=sql.Identifier('username'),
                password=sql.Identifier('password')
            ), [username, hashed_pw]
        )
    else:
        return False