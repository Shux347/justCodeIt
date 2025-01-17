from flask import Flask, render_template, request, redirect, url_for, session, flash
from database import initialize_database
from models import User, Product
from database import db
from routes.product_routes import product_bp
from routes.user_routes import user_bp
from routes.order_routes import order_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mwh_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Needed for session management

# Initialize the database
initialize_database(app)

# Register blueprints
app.register_blueprint(product_bp, url_prefix='/products')
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(order_bp, url_prefix='/orders')

@app.route('/')
def home():
    logged_in = 'user' in session
    return render_template('index.html', logged_in=logged_in)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Check if the user already exists
        if User.query.filter_by(email=email).first():
            return render_template('signup.html', error="Email already exists.")

        # Create a new user with plain-text password (not recommended for production)
        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Fetch the user from the database
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            session['user'] = {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'role': user.role,
                'voucher_balance': user.voucher_balance,
            }
            if user.role == "admin":
                return redirect(url_for('admin_page'))
            return redirect(url_for('profile'))
        else:
            return render_template('login.html', error="Invalid email or password.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

@app.route('/profile')
def profile():
    if 'user' not in session:
        return redirect(url_for('login'))
    user = session['user']
    return render_template('profile.html', user=user)

@app.route('/catalogue')
def catalogue():
    from models import Product
    products = Product.query.all()
    is_admin = False  # Default to False
    
    # Check if user session exists and if the user is an admin
    if 'user' in session:
        user = User.query.get(session['user']['id'])
        is_admin = user.role == 'admin'
    
    return render_template('catalogue.html', products=products, is_admin=is_admin)

@app.route('/admin')
def admin_page():
    # Check if the user is logged in
    if 'user' not in session:
        return redirect(url_for('login'))

    # Check if the logged-in user is an admin
    user = session['user']
    if user['role'] != 'admin':
        return render_template('error.html', message="Access denied. Admins only.")

    # Render the admin-only page
    return render_template('admin.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/add_product', methods=['POST'])
def add_product():
    if request.is_json:
        data = request.get_json()  # Parses the JSON data sent to the server
        name = data['name']
        price = data['price']
        quantity = data['quantity']

        new_product = Product(name=name, price=price, quantity=quantity)
        db.session.add(new_product)
        db.session.commit()
        flash('Product added successfully!')
        return jsonify({'message': 'Product added successfully!'}), 200
    else:
        return jsonify({'error': 'Request must be JSON'}), 400