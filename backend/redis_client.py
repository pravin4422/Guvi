import redis
import secrets

redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

def create_session(user_id):
    token = secrets.token_hex(32)
    redis_client.setex(token, 3600, str(user_id))
    return token

def get_session(token):
    user_id = redis_client.get(token)
    return int(user_id) if user_id else None

def delete_session(token):
    redis_client.delete(token)
