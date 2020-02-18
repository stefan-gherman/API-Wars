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


@db_connection.connection_handler
def login_user(cursor, username, password):
    cursor.execute(
        sql.SQL('SELECT {usrnam}, {password} from {userbase} WHERE {usrnam} = (%s) ;')
            .format(
            userbase=sql.Identifier('userbase'),
            usrnam=sql.Identifier('username'),
            password=sql.Identifier('password')
        ), [username]
    )

    result = cursor.fetchall()
    hashed_pw = result[0]['password']

    if utils.check_hashed_password(hashed_pw, password):
        return True
    else:
        return False


@db_connection.connection_handler
def return_users(cursor):
    cursor.execute(
        sql.SQL('SELECT {usrnam} FROM {userbase};')
            .format(
            usrnam=sql.Identifier('username'),
            userbase=sql.Identifier('userbase')
        ), []
    )

    query_result = cursor.fetchall()

    return query_result


@db_connection.connection_handler
def return_user_id(cursor, username):
    cursor.execute(
        sql.SQL('SELECT {id} FROM {userbase} WHERE {usrnam} = (%s);')
            .format(
            id=sql.Identifier('id'),
            userbase=sql.Identifier('userbase'),
            usrnam=sql.Identifier('username')
        ), [username]
    )

    query_result = cursor.fetchall()
    id_usr = query_result[0]['id']
    return id_usr

