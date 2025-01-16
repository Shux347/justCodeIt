from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def initialize_database(app):
    db.init_app(app)  # Bind the SQLAlchemy instance to the Flask app
    with app.app_context():
        db.create_all()  # Create tables if they don't exist