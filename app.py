from flask import Flask, render_template
from database import db, initialize_database
from routes.product_routes import product_bp
from routes.user_routes import user_bp
from routes.order_routes import order_bp

app = Flask(__name__)
app.config.from_object('config.Config')

# Initialize the database
initialize_database(app)

# Register blueprints
app.register_blueprint(product_bp, url_prefix='/products')
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(order_bp, url_prefix='/orders')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)