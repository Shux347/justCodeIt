from database import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'resident' or 'admin'
    voucher_balance = db.Column(db.Integer, default=0)

    def earn_vouchers(self, amount):
        self.voucher_balance += amount

    def spend_vouchers(self, amount):
        if self.voucher_balance >= amount:
            self.voucher_balance -= amount
        else:
            raise ValueError("Insufficient vouchers")


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)  # Price in vouchers
    quantity = db.Column(db.Integer, default=0)

    def update_stock(self, sold_quantity):
        if self.quantity >= sold_quantity:
            self.quantity -= sold_quantity
        else:
            raise ValueError("Insufficient stock")


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)


class VoucherTransaction(db.Model):
    __tablename__ = 'voucher_transactions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    transaction_type = db.Column(db.String(20), nullable=False)  # 'earned' or 'spent'
    amount = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)