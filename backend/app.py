from flask import Flask
from flask_cors import CORS
from routes.auth import auth_bp
from routes.profile import profile_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(profile_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
