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


@app.route('/users/<int:user_id>', methods=['GET'])
def user_by_id(user_id):
    user = list(filter(lambda x: x['id'] == user_id, get_users()))
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
    return jsonify({'user': user}), 201


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_by_id(user_id):
    users = get_users()
    user = list(filter(lambda x: x['id'] == user_id, users))
    users.remove(user)
    update_file(users)
    return jsonify({'user': user}), 200


if __name__ == '__main__':
    app.run(debug=True)
