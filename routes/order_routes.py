from flask import Blueprint, request, jsonify
from database import db
from models import Order, Product, User

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/place', methods=['POST'])
def place_order():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    user = User.query.get(user_id)
    product = Product.query.get(product_id)

    if not user:
        return jsonify({"error": "User not found"}), 404
    if not product:
        return jsonify({"error": "Product not found"}), 404
    if product.quantity < quantity:
        return jsonify({"error": "Insufficient stock"}), 400

    # Check voucher balance
    total_cost = product.price * quantity
    if user.voucher_balance < total_cost:
        return jsonify({"error": "Insufficient voucher balance"}), 400

    # Deduct voucher balance and update stock
    user.voucher_balance -= total_cost
    product.quantity -= quantity

    # Create the order
    order = Order(user_id=user.id, product_id=product.id, quantity=quantity)
    db.session.add(order)
    db.session.commit()

    return jsonify({"message": "Order placed successfully"})

@order_bp.route('/history/<int:user_id>', methods=['GET'])
def order_history(user_id):
    orders = Order.query.filter_by(user_id=user_id).all()
    return jsonify([{
        "order_id": order.id,
        "product_id": order.product_id,
        "quantity": order.quantity,
        "order_date": order.order_date
    } for order in orders])