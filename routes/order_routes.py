from flask import Blueprint, request, jsonify
from models import db, User, Product, Order

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/place', methods=['POST'])
def place_order():
    data = request.json
    user = User.query.get(data['user_id'])
    product = Product.query.get(data['product_id'])

    if not user or not product:
        return jsonify({"error": "Invalid user or product ID"}), 400

    total_price = product.price * data['quantity']
    if total_price > user.voucher_balance:
        return jsonify({"error": "Insufficient vouchers"}), 400

    try:
        user.spend_vouchers(total_price)
        product.update_stock(data['quantity'])

        order = Order(user_id=user.id, product_id=product.id, quantity=data['quantity'])
        db.session.add(order)
        db.session.commit()
        return jsonify({"message": "Order placed successfully"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400