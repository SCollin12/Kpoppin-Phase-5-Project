from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import CheckConstraint
from sqlalchemy.ext.hybrid import hybrid_property

# from app import bcrypt
from flask_bcrypt import Bcrypt
from config import db

bcrypt = Bcrypt()

# Models go here!

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    _password_hash = db.Column(db.String)

    orders= db.relationship('Order', backref='user', cascade='all, delete-orphan')

    serialize_only = ('id', 'username', 'email', 'password_hash')




    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise ValueError("Username must be present")
        return username

    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        if type(password) is str and len(password) > 6:
            password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
            self._password_hash = password_hash.decode('utf-8')
        else:
            raise ValueError("Password Invalid")
    
    def authenticate(self, password):
        from app import bcrypt
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise ValueError("Email must be present")
        return email


class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Numeric (10 ,2))
    release_date = db.Column(db.Date)  # date values should be in the format of 'YYYY-MM-DD'
    image_url = db.Column(db.String)
    type = db.Column(db.String(10), CheckConstraint("type IN ('anime', 'kpop')"), nullable=False)
    serialize_only = ('id', 'name', 'description', 'price', 'release_date', 'image_url', 'type')

     
    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Name must be present")
        return name

    @validates('price')
    def validate_price(self, key, price):
            price = float(price)
            if  0.00 < price <= 50.00:
                
                return price    
            else:  
                raise ValueError("Price must be between 0 and 50")




    


class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    status = db.Column(db.String, default='In Progress')

    __table_args__ = (
        CheckConstraint(
            "status IN ('In Progress', 'Completed', 'Cancelled', 'Shipped')",
            name="check_order_status"
        ),
    )

    order_products = db.relationship('Order_product', backref='order', cascade='all, delete-orphan')

    serialize_only = ('id', 'user_id', 'status', 'order_products')


    @validates('status')
    def validate_status(self, key, status):
        allowed_statuses = ['In Progress', 'Completed', 'Cancelled', 'Shipped']
        if status not in allowed_statuses:
            raise ValueError("Invalid order status. Status must be one of: 'In Progress', 'Completed', 'Cancelled', 'Shipped'")
        return status



class Order_product(db.Model, SerializerMixin):
    __tablename__ = 'order_product'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    # order = db.relationship('Order', backref='order_products')
    product = db.relationship('Product', backref='order_products')
    serialize_only = ('id', 'order_id', 'product_id')




    # @validates('order_id', 'product_id')
    # def validate_order_product_ids(self, key, value):
    #     if not value or value < 1:
    #         raise ValueError(f"{key.capitalize()} must be a positive integer")

    
    #     if key == 'order_id' and not Order.query.get(value):
    #         raise ValueError("Order with the specified ID does not exist")
    #     elif key == 'product_id' and not Product.query.get(value):
    #         raise ValueError("Product with the specified ID does not exist")

    #         return value




class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    comments = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    user = db.relationship('User', backref='reviews')
    product = db.relationship('Product', backref='reviews')
    serialize_only = ('id', 'comments', 'user_id', 'product_id')


    # @validates('product_id')
    # def validate_workout(self, key, product_id):
    #     if not product_id or product_id < 1:
    #         raise ValueError("Product ID must be present and greater than 0")
    #     return product_id

    # @validates('user_id')
    # def validate_user(self, key, user_id):
    #     if not user_id or user_id < 1:
    #         raise ValueError("User ID must be present and greater than 0")
    #     return user_id
        
    @validates('comments')
    def validate_comments(self, key, comments):
        if comments is None or len(comments) < 10:
            raise ValueError("Comment must be present and at least 10 characters long")
        return comments




# the single_parent=True flag to the relationship between Review and User. 
#This flag indicates that a particular User object can be referenced by only a single Review object at a time,
#which allows the delete-orphan cascade to work in this direction.