from flask import Blueprint, request, jsonify
from models import db, Product

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/add', methods=['POST'])
def add_product():
    data = request.json
    product = Product(name=data['name'], price=data['price'], quantity=data['quantity'])
    db.session.add(product)
    db.session.commit()
    return jsonify({"message": "Product added successfully"}), 201

@product_bp.route('/list', methods=['GET'])
def list_products():
    products = Product.query.all()
    return jsonify([{"id": p.id, "name": p.name, "price": p.price, "quantity": p.quantity} for p in products])