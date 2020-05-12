import json
from exercice2 import add_user, get_users, connect_db, add_users, search_user, get_one_user


def test_add_user_test():
    user = [4, 'HAMZA', 'MENSI', '+33621432483']
    add_user(user)
    conn, cursor = connect_db()
    cursor.execute('SELECT * from utilisateur where id = 4')
    user_sql = cursor.fetchone()
    assert user_sql[0] == user[0]
    assert user_sql[1] == user[1]
    assert user_sql[2] == user[2]
    assert user_sql[3] == user[3]

def test_get_users():
    get_users()
    with open('users.json', 'r+') as f:
        users = json.loads(f.read())
        conn, cursor = connect_db()
        cursor.execute('SELECT * from utilisateur')
        users_sql = cursor.fetchall()
        user_json = [{'id': user_sql[0], 'first_name': user_sql[1], 'last_name': user_sql[2], 'phone_number': user_sql[3]} for user_sql in users_sql]
        assert user_json == users

def test_get_one_user():
    user = get_one_user()
    with open('id.json', 'r+') as f:
        id = json.loads(f.read()).get('id')
        conn, cursor = connect_db()
        cursor.execute('SELECT * from utilisateur where id = %s' % (id))
        user_sql = cursor.fetchone()
        user_json = {
            'id': user_sql[0],
            'first_name': user_sql[1],
            'last_name': user_sql[2],
            'phone_number': user_sql[3]
        }
        user = {
            'id': user[0],
            'first_name': user[1],
            'last_name': user[2],
            'phone_number': user[3]
        }
        assert user == user_json


def test_add_users():
    add_users('users_to_add.json')
    with open('users.json', 'r+') as f:
        users = json.loads(f.read())
        conn, cursor = connect_db()
        cursor.execute('SELECT * from utilisateur')
        users_sql = cursor.fetchall()
        user_json = [{'id': user_sql[0], 'first_name': user_sql[1], 'last_name': user_sql[2], 'phone_number': user_sql[3]} for user_sql in users_sql]
        for user in users:
            assert user in user_json


def test_search_user():
    search_user(['first_name', 'XX'])
    with open('users_search.json', 'r+') as f:
        users = json.loads(f.read())
        conn, cursor = connect_db()
        cursor.execute("SELECT * from utilisateur where first_name = 'XX'")
        users_sql = cursor.fetchall()
        user_json = [{'id': user_sql[0], 'first_name': user_sql[1], 'last_name': user_sql[2], 'phone_number': user_sql[3]} for user_sql in users_sql]
        assert users == user_json
