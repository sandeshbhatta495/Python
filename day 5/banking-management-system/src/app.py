from flask import Flask
from routes.auth import auth_bp
from routes.banking import banking_bp
from database.db import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(banking_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)