#!flask/bin/python
from flask import Flask, jsonify, request, abort
import json

app = Flask(__name__)

USERS_PATH = 'data/users.json'


def get_users():
    return list(json.loads(open(USERS_PATH).read()))


def update_file(users):
    with open(USERS_PATH, 'w') as users_file:
        json.dump(users, users_file)


@app.route('/')
def index():
    return {
        "status": "ok"
    }


@app.route('/login-plain', methods=['POST'])
def login_plain():
    return jsonify({"status": "Success", "token": "1asd81wq691dqw61ds3a51d3wa1"}), 200


@app.route('/login-post', methods=['POST'])
def login_post():
    if not request.json:
        return jsonify({"status": "Unauthorized"}), 401
    # This is not a real login situation
    if request.json.username == 'username' and request.json.password == 'password':
        return jsonify({"status": "Success", "token": "1asd81wq691dqw61ds3a51d3wa1"}), 200
    else:
        return jsonify({"status": "Forbidden"}), 403


@app.route('/login-get', methods=['GET'])
def login_get():
    return jsonify({"status": "Success", "token": "1asd81wq691dqw61ds3a51d3wa1"}), 200


@app.route('/users/<int:user_id>', methods=['GET'])
def user_by_id(user_id):
    user = list(filter(lambda x: x['id'] == user_id, get_users()))[0]
    return jsonify(user), 200


@app.route('/users', methods=['GET'])
def users():
    return jsonify(get_users()), 200


@app.route('/users', methods=['POST'])
def add_user():
    if not request.json or not 'username' in request.json:
        abort(400)

    users = get_users()
    last_id = users[-1]['id'] if len(users) > 0 else 0
    user = {
        'id': last_id + 1,
        'username': request.json.get('username', None),
        'name': request.json.get('name', ""),
        'surname': request.json.get('surname', ""),
        'email': request.json.get('email', "")
    }
    users.append(user)

    update_file(users)
    return jsonify(user), 201


@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    if not request.json or user_id is None:
        abort(400)
    users = get_users()
    user = list(filter(lambda x: x['id'] == user_id, users))[0]
    index = users.index(user)

    new_username = request.json.get('username', None)
    new_name = request.json.get('name', None)
    new_surname = request.json.get('surname', None)
    new_email = request.json.get('email', None)

    if new_username:
        users[index]['username'] = new_username
    if new_name:
        users[index]['name'] = new_name
    if new_surname:
        users[index]['surname'] = new_surname
    if new_email:
        users[index]['email'] = new_email

    update_file(users)
    return jsonify(users[index]), 200


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_by_id(user_id):
    users = get_users()
    user = list(filter(lambda x: x['id'] == user_id, users))[0]
    users.remove(user)
    update_file(users)
    return jsonify(user), 200


if __name__ == '__main__':
    app.run(debug=True)
