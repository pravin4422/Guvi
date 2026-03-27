from flask import Blueprint, request, jsonify
from redis_client import get_session
from mongo_client import get_profile, update_profile

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile', methods=['GET'])
def get_user_profile():
    token = request.headers.get('Authorization')
    user_id = get_session(token)
    
    if not user_id:
        return jsonify({'error': 'Unauthorized'}), 401
    
    profile = get_profile(user_id)
    if profile:
        return jsonify(profile), 200
    return jsonify({'age': '', 'dob': '', 'contact': ''}), 200

@profile_bp.route('/profile', methods=['PUT'])
def update_user_profile():
    token = request.headers.get('Authorization')
    user_id = get_session(token)
    
    if not user_id:
        return jsonify({'error': 'Unauthorized'}), 401
    
    data = request.get_json()
    age = data.get('age')
    dob = data.get('dob')
    contact = data.get('contact')
    
    update_profile(user_id, age, dob, contact)
    return jsonify({'message': 'Profile updated'}), 200
