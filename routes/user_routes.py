from flask import Blueprint, request, jsonify
from models import db, User

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/add', methods=['POST'])
def add_user():
    data = request.json
    user = User(name=data['name'], email=data['email'], password=data['password'], role=data['role'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User added successfully"}), 201

@user_bp.route('/list', methods=['GET'])
def list_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email, "role": u.role, "voucher_balance": u.voucher_balance} for u in users])