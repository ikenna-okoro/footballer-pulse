from flask import Flask
from sqlalchemy import text
from repository.fan_models import db
from controller.my_blueprints import bp



# Configure the app
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fanscomments.db'
    db.init_app(app)
    app.register_blueprint(bp, url_prefix='/footballer-pulse')

    with app.app_context():
        db.create_all()

    return app