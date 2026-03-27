from flask import Blueprint, request, jsonify
from db import register_user, verify_user
from redis_client import create_session

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    
    try:
        user_id = register_user(name, email, password)
        return jsonify({'message': 'Registration successful'}), 201
    except:
        return jsonify({'error': 'Registration failed'}), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    user_id = verify_user(email, password)
    if user_id:
        token = create_session(user_id)
        return jsonify({'token': token}), 200
    return jsonify({'error': 'Invalid credentials'}), 401
