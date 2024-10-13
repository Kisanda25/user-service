from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    #Load the app configurations 
    app.config.from_object('app.config.config')

    #initialise the database and the migration tools 
    db.init_app(app)
    migrate = Migrate(app, db)

    #Register the routes 
    from app.routes import user_bp
    app.register_blueprint(user_bp)

    return app


