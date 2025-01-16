from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def initialize_database(app):
    db.init_app(app)  # Bind the SQLAlchemy instance to the Flask app
    with app.app_context():
        db.create_all()  # Create tables if they don't exist

        # Import models after `db` is initialized to avoid circular imports
        from models import User

        # Check if admin user already exists
        admin_email = "admin@login"
        if not User.query.filter_by(email=admin_email).first():
            admin_user = User(
                name="Admin",
                email=admin_email,
                password="Admin",  # Plain-text for simplicity; use hashing in production
                role="admin"
            )
            db.session.add(admin_user)
            db.session.commit()
            print(f"Admin account created: {admin_email} / Password: Admin")
