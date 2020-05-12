import json
from exercice2 import add_user, get_users, connect_db, add_users, search_user, get_one_user


def add_user_test():
    user = {
        'id': 4,
        'first_name': 'Hamza',
        'last_name': 'MENSI',
        'phone_number': '+33621432483'
    }
    add_user(user)
    conn, cursor = connect_db()
    cursor.execute('SELECT * from utilisateur where id = 4')
    user = cursor.fetchone()
    assert user[0] == user.get('id')
    assert user[1] == user.get('first_name')
    assert user[2] == user.get('last_name')
    assert user[3] == user.get('phone_number')

def get_users_test():
    get_users()
    with open('users.json', 'r+') as f:
        users = json.loads(f.read())
        conn, cursor = connect_db()
        cursor.execute('SELECT * from utilisateur')
        users = cursor.fetchall()
        user_json = [{'id': user_sql[0], 'first_name': user_sql[1], 'last_name': user_sql[2], 'phone_number': user_sql[3]} for user_sql in users]
        assert user_json == users

def get_one_user_test():
    get_one_user()
    with open('id.json', 'r+') as f:
        user = json.loads(f.read()).get('id')
        conn, cursor = connect_db()
        cursor.execute('SELECT * from utilisateur where id = %s' % (user))
        user_sql = cursor.fetchone()
        user_json = {
            'id': user_sql[0],
            'first_name': user_sql[1],
            'last_name': user_sql[2],
            'phone_number': user_sql[3]
        }
        assert user == user_json


def add_users_test():
    add_users()
    with open('users.json', 'r+') as f:
        users = json.loads(f.read())
        conn, cursor = connect_db()
        cursor.execute('SELECT * from utilisateur')
        users_sql = cursor.fetchall()
        user_json = [{'id': user_sql[0], 'first_name': user_sql[1], 'last_name': user_sql[2], 'phone_number': user_sql[3]} for user_sql in users_sql]
        for user in users:
            assert user in user_json

def search_user_test():
    search_user(['first_name', 'XX'])
    with open('users.json', 'r+') as f:
        users = json.loads(f.read())
        conn, cursor = connect_db()
        cursor.execute("SELECT * from utilisateur where first_name = 'XX'")
        users_sql = cursor.fetchall()
        user_json = [{'id': user_sql[0], 'first_name': user_sql[1], 'last_name': user_sql[2], 'phone_number': user_sql[3]} for user_sql in users_sql]
        assert users == user_json
