import sqlite3
import sys
import json

def connect_db ():
    try:
        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()
        return sqliteConnection, cursor
    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)


def add_user(user):
    connection = None
    try:
        sql_request = "INSERT INTO utilisateur (id, first_name, last_name, phone_number) " \
                 "VALUES (%s, '%s', '%s', '%s')" % (user[0],
                                                    user[1],
                                                    user[2],
                                                    user[3]
                                                    )
        connection, cursor = connect_db()
        cursor.execute(sql_request)

        connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        if (connection):
            connection.close()
            print("sqlite connection is closed")

def get_users():
    connection = None
    try:
        sql_request = "SELECT * FROM utilisateur"
        connection, cursor = connect_db()
        cursor.execute(sql_request)
        users_sql = cursor.fetchall()
        user_json = [{'id': user_sql[0], 'first_name': user_sql[1], 'last_name': user_sql[2], 'phone_number': user_sql[3]} for user_sql in users_sql]
        with open('users.json', 'w+') as f:
            f.write(json.dumps(user_json))
            f.close()
        cursor.close()
    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        if (connection):
            connection.close()
        print("sqlite connection is closed")


def get_one_user():
    connection = None
    with open('id.json', 'r+') as f:
        user = json.loads(f.read())
        try:
            sql_request = "SELECT * FROM utilisateur where id = %s" % (user.get('id'))
            connection, cursor = connect_db()
            cursor.execute(sql_request)
            user_sql = cursor.fetchone()
            print('%s %s %s %s' %(user_sql[0], user_sql[1], user_sql[2], user_sql[3]))
            return user_sql
        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if (connection):
                connection.close()

def add_users(file):
    with open(file, 'r+') as f:
        users = json.loads(f.read())
        try:
            connection, cursor = connect_db()
            for user in users:
               sql_request = "INSERT INTO utilisateur (id, first_name, last_name, phone_number) " \
                             "VALUES (%s, '%s', '%s', '%s')" % (user.get('id'),
                                                                user.get('first_name'),
                                                                user.get('last_name'),
                                                                user.get('phone_number')
                                                                )

               cursor.execute(sql_request)
            connection.commit()
            cursor.close()
        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if (connection):
                connection.close()

def search_user(args):
    connection = None
    column_name = args[0]
    value = args[1]
    try:
        sql_request = "SELECT * FROM utilisateur where %s = '%s'" % (column_name, value)
        connection, cursor = connect_db()
        cursor.execute(sql_request)
        users_sql = cursor.fetchall()
        user_json = [{'id': user_sql[0], 'first_name': user_sql[1], 'last_name': user_sql[2], 'phone_number': user_sql[3]} for user_sql in users_sql]
        with open('users_search.json', 'w+') as f:
            f.write(json.dumps(user_json))
            f.close()
    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        if (connection):
            connection.close()

if __name__ == '__main__':
    args = sys.argv[1:]
    if args[0] == 'add_user':
        add_user(args[1:])
    elif args[0] == 'get_users':
        get_users()
    elif args[0] == 'get_one':
        get_one_user()
    elif args[0] == 'add_users':
        add_users(args[2])
    elif args[0] == 'search':
        search_user(args[1:])
