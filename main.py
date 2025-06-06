from flask import Flask
from sqlalchemy import text
from repository.fan_models import db
from my_blueprints import bp



# Configure the app
if __name__ == "__main__":
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fanscomments.db'
    db.init_app(app)
    app.register_blueprint(bp, url_prefix='/footballer-pulse')

    with app.app_context():
        db.create_all()

    with app.app_context():
        result = db.session.execute(text("SELECT * FROM fans_comments"))
        for row in result:
            print(row)
    
    app.run(debug=True)