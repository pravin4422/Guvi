from pymongo import MongoClient

mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['secureauth']
profiles = db['profiles']

def get_profile(user_id):
    return profiles.find_one({'user_id': user_id}, {'_id': 0, 'user_id': 0})

def update_profile(user_id, age, dob, contact):
    profiles.update_one(
        {'user_id': user_id},
        {'$set': {'age': age, 'dob': dob, 'contact': contact}},
        upsert=True
    )
