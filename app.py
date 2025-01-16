from flask import Flask
from database import initialize_database
from user_routes import user_bp
from product_routes import product_bp
from order_routes import order_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mwh_app.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
initialize_database(app)

# Register blueprints
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(product_bp, url_prefix='/products')
app.register_blueprint(order_bp, url_prefix='/orders')

@app.route('/')
def home():
    return "MWH Mini-mart Backend is Running!"

if __name__ == '__main__':
    app.run(debug=True)