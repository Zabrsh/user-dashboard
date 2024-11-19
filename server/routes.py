from flask import request, jsonify
from server import app
from server.models import User, save_users, load_users

users = load_users()

@app.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()
    email = data.get('email')
    if email in users:
        return jsonify({'message': 'User already exists'}), 400
    users[email] = User(email, data.get('age')).to_dict()
    save_users(users)
    return jsonify({'message': 'User added successfully'}), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/user/<email>', methods=['GET'])
def get_user(email):
    user = users.get(email)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user), 200

@app.route('/user/<email>', methods=['DELETE'])
def delete_user(email):
    if email in users:
        del users[email]
        save_users(users)
        return jsonify({'message': 'User deleted successfully'}), 200
    return jsonify({'message': 'User not found'}), 404

@app.route('/user/<email>', methods=['PUT'])
def update_user(email):
    if email not in users:
        return jsonify({'message': 'User not found'}), 404
    data = request.get_json()
    users[email]['age'] = data.get('age', users[email]['age'])
    save_users(users)
    return jsonify({'message': 'User updated successfully'}), 200