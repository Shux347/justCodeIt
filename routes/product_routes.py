from flask import Blueprint, request, jsonify
from database import db
from models import Product

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/add', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    quantity = data.get('quantity')

    product = Product(name=name, price=price, quantity=quantity)
    db.session.add(product)
    db.session.commit()
    return jsonify({"message": "Product added successfully"}), 201

@product_bp.route('/list', methods=['GET'])
def list_products():
    products = Product.query.all()
    return jsonify([{
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity
    } for product in products])

@product_bp.route('/update/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = Product.query.get(product_id)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    product.name = data.get('name', product.name)
    product.price = data.get('price', product.price)
    product.quantity = data.get('quantity', product.quantity)
    db.session.commit()
    return jsonify({"message": "Product updated successfully"})