#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from models import *
from flask_restful import Api, Resource
from flask import Flask, make_response, jsonify, request, session
from flask_migrate import Migrate
import os
from flask_bcrypt import Bcrypt
from faker import Faker
from datetime import datetime
from dateutil.parser import parse
# Local imports
from config import app, db, api
# Add your model imports

fake = Faker()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
migrate = Migrate(app, db)

db.init_app(app)

bcrypt = Bcrypt(app)

api = Api(app)
# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

class Users(Resource):
    def get(self):
        users = [user.to_dict(only=('id', 'username', 'email')) for user in User.query.all()]
        return make_response(users, 200)


    def post(self):
        try:
            username = request.json.get('username')
            email = request.json.get('email')
            password = request.json.get('password')  # Change this to 'password'

            if not username or not email or not password:
                return {"errors": ["Missing username, email, or password"]}, 400

            # Hash the password
            password_hash = bcrypt.generate_password_hash(password.encode('utf-8')).decode('utf-8')

            new_user = User(username=username, email=email, password_hash=password_hash)
            db.session.add(new_user)
            db.session.commit()
            return make_response(new_user.to_dict(only=('id', 'username', 'email')), 201)
        except Exception as e:
            return {"errors": [str(e)]}, 400

api.add_resource(Users, '/users')


class UsersById(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            return make_response({"error": ["User not found"]}, 404)
        user_to_dict = user.to_dict(only=('id', 'username', 'email'))
        return make_response(user_to_dict, 200)

    def patch(self, id):
        user = User.query.filter_by(id = id).first()
        if not user:
            return make_response({"error": ["User not found"]}, 404)
        try:
            for attr in request.json: 
                setattr(user, attr, request.json[attr])
            db.session.add(user)
            db.session.commit()
            user_to_dict = user.to_dict(only=('id', 'username', 'email'))
            return make_response(user_to_dict, 202)
        except ValueError:
            return make_response({"errors":["validation errors"]}, 400)

    def delete(self,id):
        user = User.query.filter_by(id = id).first()
        if not user:
            return make_response({"error": ["User not found"]}, 404)
        db.session.delete(user)
        db.session.commit()
        return make_response({}, 204)
api.add_resource(UsersById, '/users/<int:id>')

class Products(Resource):
    def get(self):
        products = [product.to_dict(only=('id', 'name', 'description', 'price', 'release_date', 'image_url', 'type')) for product in Product.query.all()]
        return make_response(products, 200)

    def post(self):
        try:
            name = request.json['name']
            description = request.json['description']
            price = request.json['price']
            
            # Convert the release_date string to a Python date object
            release_date_str = request.json['release_date']
            release_date = parse(release_date_str).date()

            image_url = request.json['image_url']
            type = request.json['type']

            new_product = Product(
                name=name,
                description=description,
                price=price,
                release_date=release_date,
                image_url=image_url,
                type=type
            )
            db.session.add(new_product)
            db.session.commit()
            return make_response(new_product.to_dict(), 201)
        except ValueError:
            return {"errors": ["Validation errors"]}, 400



api.add_resource(Products, '/products')

class ProductsById(Resource):
    def get(self, id):
        product = Product.query.filter_by(id=id).first()
        if not product:
            return make_response({"error": ["Product not found"]}, 404)
        product_to_dict = product.to_dict()
        return make_response(product_to_dict, 200)

    def patch(self, id):
        product = Product.query.filter_by(id=id).first()
        if not product:
            return make_response({"error": ["Product not found"]}, 404)
        try:
            for attr in request.json:
                setattr(product, attr, request.json[attr])
            db.session.add(product)
            db.session.commit()
            product_to_dict = product.to_dict(only = ('id', 'name', 'description', 'price', 'release_date', 'image_url', 'type'))
            return make_response(product_to_dict, 202)
        except ValueError:
            return make_response({"errors": ["Validation errors"]}, 400)

    def delete(self, id):
        product = Product.query.filter_by(id=id).first()
        if not product:
            return make_response({"error": ["Product not found"]}, 404)
        db.session.delete(product)
        db.session.commit()
        return make_response({}, 204)

api.add_resource(ProductsById, '/products/<int:id>')

class Orders(Resource):
    def get(self):
        orders = [order.to_dict(only = ('id', 'user_id', 'status', 'order_products')) for order in Order.query.all()]
        return make_response(orders, 200)

    def post(self):
        try:
            new_order = Order()
            db.session.add(new_order)
            db.session.commit()
            return make_response(new_order.to_dict(), 201)
        except ValueError:
            return make_response({"errors": ["Validation errors"]}, 400)
api.add_resource(Orders, '/orders')


class OrdersById(Resource):
    def get(self, id):
        order = Order.query.filter_by(id=id).first()
        if not order:
            return make_response({"error": ["Order not found"]}, 404)
        order_to_dict = order.to_dict()
        return make_response(order_to_dict, 200)

    def patch(self, id):
        order = Order.query.filter_by(id=id).first()
        if not order:
            return make_response({"error": ["Order not found"]}, 404)
        try:
            for attr in request.json:
                setattr(order, attr, request.json[attr])
            db.session.add(order)
            db.session.commit()
            return make_response(order_to_dict(only = ('id', 'user_id', 'status', 'order_products')), 202)
        except ValueError:
            return make_response({"errors": ["Validation errors"]}, 400)

    def delete(self, id):
        order = Order.query.filter_by(id=id).first()
        if not order:
            return make_response({"error": ["Order not found"]}, 404)
        db.session.delete(order)
        db.session.commit()
        return make_response({}, 204)

api.add_resource(OrdersById, '/orders/<int:id>')

class OrderProducts(Resource):
    def get(self):
        order_products= [op.to_dict(only = ('id', 'order_id', 'product_id')) for op in Order_product.query.all()]
        return make_response(order_products, 200)

    def post(self):
        try:
            new_order_product = Order_product()
            db.session.add(new_order_product)
            db.session.commit()
            return make_response(new_order_product.to_dict(), 201)
        except ValueError:
            return make_response({"errors": ["Validation errors"]}, 400)

api.add_resource(OrderProducts, '/order_products')


class OrderProductsById(Resource):
    def get(self, id):
        order_product = Order_product.query.filter_by(id=id).first()
        if not order_product:
            return make_response({"error": ["Order_product not found"]}, 404)
        order_product_to_dict = order_product.to_dict(serialize_only = ('id', 'order_id', 'product_id'))
        return make_response(order_product_to_dict, 200)

    def patch(self, id):
        order_product = Order_product.query.filter_by(id=id).first()
        if not order_product:
            return make_response({"error": ["Order_product not found"]}, 404)
        try:
            for attr in request.json:
                setattr(order_product, attr, request.json[attr])
            db.session.add(order_product)
            db.session.commit()
            return make_response(order_product_to_dict(serialize_only = ('id', 'order_id', 'product_id')), 202)
        except ValueError:
            return make_response({"errors": ["Validation errors"]}, 400)

    def delete(self, id):
        order_product = Order_product.query.filter_by(id=id).first()
        if not order_product:
            return make_response({"error": ["Order_product not found"]}, 404)
        db.session.delete(order_product)
        db.session.commit()
        return make_response({}, 204)

api.add_resource(OrderProductsById, '/order_products/<int:id>')


class Reviews(Resource):
    def get(self):
        reviews = [review.to_dict(only = ('id', 'comments', 'user_id', 'product_id')) for review in Review.query.all()]
        return make_response(reviews, 200)

    def post(self):
        try:
            new_review = Review(
                comments=request.json['comments'],
                user_id=request.json['user_id'],
                product_id=request.json['product_id']
            )
            db.session.add(new_review)
            db.session.commit()
            return make_response(new_review.to_dict(), 201)
        except ValueError:
            return {"errors": ["Validation errors"]}, 400
api.add_resource(Reviews, '/reviews')


class ReviewsById(Resource):
    def get(self, id):
        review = Review.query.filter_by(id=id).first()
        if not review:
            return make_response({"error": ["Review not found"]}, 404)
        review_to_dict = review.to_dict(serialize_only = ('id', 'comments', 'user_id', 'product_id'))
        return make_response(review_to_dict, 200)

    def patch(self, id):
        review = Review.query.filter_by(id=id).first()
        if not review:
            return make_response({"error": ["Review not found"]}, 404)
        try:
            for attr in request.json:
                setattr(review, attr, request.json[attr])
            db.session.add(review)
            db.session.commit()
            return make_response(review_to_dict(serialize_only = ('id', 'comments', 'user_id', 'product_id')), 202)
        except ValueError:
            return make_response({"errors": ["Validation errors"]}, 400)

    def delete(self, id):
        review = Review.query.filter_by(id=id).first()
        if not review:
            return make_response({"error": ["Review not found"]}, 404)
        db.session.delete(review)
        db.session.commit()
        return make_response({}, 204)
api.add_resource(ReviewsById, '/reviews/<int:id>')

class Login(Resource):
    def post(self):
        user = User.query.filter(User.username == request.json['username']).first()
        password = request.json['password']
        if user and user.authenticate(password):
            session['user_id'] = user.id
            return make_response(user.to_dict(rules=('-_password_hash',)), 201)
        else:
            return make_response('error', 400)

api.add_resource(Login, '/login')

class Signup(Resource):
    def post(self):
        try:
            new_user = User(
                username = request.json['username'],
                email = request.json['email'],
                password_hash = request.json['password'],
            )
            db.session.add(new_user)
            db.session.commit()
            session['user_id'] = new_user.id
            return make_response(new_user.to_dict(rules=('-_password_hash',)), 201)
        except ValueError:
            return make_response({"error": "User not created"}, 400)

api.add_resource(Signup, '/signup')

class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        return make_response({}, 204)

api.add_resource(Logout, '/logout')

class AutoLogin(Resource):
    def get(self):
        if session['user_id']:
            user = User.query.filter(User.id == session['user_id']).first()
            if user:
                return make_response(user.to_dict(rules=('-_password_hash',)), 200)
            else:
                return make_response({"errors": "User not found"}, 404)
        else:
            return make_response('', 204)

api.add_resource(AutoLogin, '/auto_login')

if __name__ == '__main__':
    app.run(port=5555, debug=True) 



























if __name__ == '__main__':
    app.run(port=5555, debug=True)

