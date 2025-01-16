from datetime import datetime
from database import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='resident')  # 'resident' or 'admin'
    voucher_balance = db.Column(db.Integer, default=0)

    # Relationships
    orders = db.relationship('Order', backref='user', lazy=True)
    transactions = db.relationship('VoucherTransaction', backref='user', lazy=True)

    # Methods for voucher management
    def earn_vouchers(self, amount):
        """Add vouchers to the user's balance."""
        if amount < 0:
            raise ValueError("Amount to earn must be positive")
        self.voucher_balance += amount
        db.session.commit()

    def spend_vouchers(self, amount):
        """Deduct vouchers from the user's balance."""
        if amount < 0:
            raise ValueError("Amount to spend must be positive")
        if self.voucher_balance < amount:
            raise ValueError("Insufficient vouchers")
        self.voucher_balance -= amount
        db.session.commit()

    def __repr__(self):
        return f"<User {self.name}, Email: {self.email}, Role: {self.role}, Vouchers: {self.voucher_balance}>"

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)  # Price in vouchers
    quantity = db.Column(db.Integer, nullable=False, default=0)

    # Relationships
    orders = db.relationship('Order', backref='product', lazy=True)

    # Methods for stock management
    def reduce_stock(self, quantity):
        """Reduce stock of the product."""
        if quantity < 0:
            raise ValueError("Quantity to reduce must be positive")
        if self.quantity < quantity:
            raise ValueError("Insufficient stock")
        self.quantity -= quantity
        db.session.commit()

    def increase_stock(self, quantity):
        """Increase stock of the product."""
        if quantity < 0:
            raise ValueError("Quantity to increase must be positive")
        self.quantity += quantity
        db.session.commit()

    def __repr__(self):
        return f"<Product {self.name}, Price: {self.price}, Stock: {self.quantity}>"

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)

    # Helper method to create an order
    @classmethod
    def create_order(cls, user, product, quantity):
        """Create an order and handle stock and vouchers."""
        if quantity <= 0:
            raise ValueError("Order quantity must be greater than zero")
        if product.price * quantity > user.voucher_balance:
            raise ValueError("Insufficient vouchers to place the order")
        product.reduce_stock(quantity)
        user.spend_vouchers(product.price * quantity)
        order = cls(user_id=user.id, product_id=product.id, quantity=quantity)
        db.session.add(order)
        db.session.commit()
        return order

    def __repr__(self):
        return f"<Order User: {self.user_id}, Product: {self.product_id}, Quantity: {self.quantity}, Date: {self.order_date}>"

class VoucherTransaction(db.Model):
    __tablename__ = 'voucher_transactions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    transaction_type = db.Column(db.String(20), nullable=False)  # 'earned' or 'spent'
    amount = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # Helper method to record a voucher transaction
    @classmethod
    def record_transaction(cls, user, transaction_type, amount):
        """Record a voucher transaction."""
        if transaction_type not in ['earned', 'spent']:
            raise ValueError("Invalid transaction type")
        if amount <= 0:
            raise ValueError("Transaction amount must be positive")
        transaction = cls(user_id=user.id, transaction_type=transaction_type, amount=amount)
        db.session.add(transaction)
        db.session.commit()
        return transaction

    def __repr__(self):
        return f"<VoucherTransaction User: {self.user_id}, Type: {self.transaction_type}, Amount: {self.amount}, Date: {self.timestamp}>"