from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import CheckConstraint

# from app import bcrypt

from config import db

# Models go here!

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    _password_hash = db.Column(db.String)

    orders= db.relationship('Order', backref='user', cascade='all, delete-orphan')

    serialize_rules = ('-orders',)

    # @validates('username')
    # def validate_username(self, key, username):
    #     if not username:
    #         raise ValueError("Username must be present")
    #     return username

    # @hybrid_property
    # def password_hash(self):
    #     return self._password_hash

    # @password_hash.setter
    # def password_hash(self, password):
    #     if type(password) is str and len(password) > 6:
    #         password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
    #         self._password_hash = password_hash.decode('utf-8')
    #     else:
    #         raise ValueError("Password Invalid")
    
    # def authenticate(self, password):
    #     from app import bcrypt
    #     return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))

class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    release_date = db.Column(db.Date)  # date values should be in the format of 'YYYY-MM-DD'
    image_url = db.Column(db.String)
    type = db.Column(db.String(10), CheckConstraint("type IN ('anime', 'kpop')"), nullable=False)
    serialize_rules = ('-order_products.product',)


    


class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    order_products = db.relationship('Order_product', backref='order', cascade='all, delete-orphan')
    serialize_rules = ('-order.products.orders',)

class Order_product(db.Model, SerializerMixin):
    __tablename__ = 'order_product'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    # order = db.relationship('Order', backref='order_products')
    product = db.relationship('Product', backref='order_products')
    serialize_rules = ("-product.order_products", )



class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    comments = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    user = db.relationship('User', backref='reviews')
    product = db.relationship('Product', backref='reviews', single_parent=True, cascade='all, delete-orphan')  # Set single_parent=True
    serialize_rules = ('-user.reviews', '-products.reviews').

# the single_parent=True flag to the relationship between Review and User. 
#This flag indicates that a particular User object can be referenced by only a single Review object at a time,
#which allows the delete-orphan cascade to work in this direction.
