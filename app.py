from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='build')
app.config.from_object('config.Config')

# Initialize the database
from database import db, initialize_database
initialize_database(app)

# Register blueprints
from routes.product_routes import product_bp
from routes.user_routes import user_bp
from routes.order_routes import order_bp
app.register_blueprint(product_bp, url_prefix='/products')
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(order_bp, url_prefix='/orders')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
