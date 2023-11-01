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
# Local imports
from config import app, db, api
# Add your model imports

# fake = Faker()

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
        users = User.query.all()
        users_list = [user.to_dict(only=('id', 'username', 'email')) for user in users]
        return make_response(users_list, 200)

    def post(self):
        try:
            new_user = User(
                username=request.json['username'],
                email=request.json['email'],
                password=request.json['password_hash']
            )
            db.session.add(new_user)
            db.session.commit()
            return make_response(new_user.to_dict(only=('id', 'username', 'email'))), 201
        except ValueError:
            return {"errors": ["Validation errors"]}, 400

api.add_resource(Users, '/users')


class UsersById(Resource):
    def get(self, id):
        user = User.query.filter_by(id = id).first()
        if not user:
            return make_response({"error": ["User not found"]}, 404)
        user_to_dict = user.to_dict()
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
            user_to_dict = user.to_dict()
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
        products = Product.query.all()
        products_list = [product.to_dict() for product in products]
        return make_response(products, 200)

    def post(self):
        try:
            new_product = Product(
                name=request.json['name'],
                description=request.json['description'],
                price=request.json['price'],
                release_date=request.json['release_date'],
                image_url=request.json['image_url'],
                type=request.json['type']
            )
            db.session.add(new_product)
            db.session.commit()
            return make_response(new_product.to_dict()), 201
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
            product_to_dict = product.to_dict()
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
        orders = Order.query.all()
        orders_list = [order.to_dict() for order in orders]
        return make_response(orders_list, 200)

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
            # Update order attributes from request.json
            for attr in request.json:
                setattr(order, attr, request.json[attr])
            db.session.add(order)
            db.session.commit()
            order_to_dict = order.to_dict()
            return make_response(order_to_dict, 202)
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
        # List Order_product records
        order_products = Order_product.query.all()
        order_products_list = [op.to_dict() for op in order_products]
        return make_response(order_products_list, 200)

    def post(self):
        # Create a new Order_product record
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
        # Retrieve an individual Order_product record by ID
        order_product = Order_product.query.filter_by(id=id).first()
        if not order_product:
            return make_response({"error": ["Order_product not found"]}, 404)
        order_product_to_dict = order_product.to_dict()
        return make_response(order_product_to_dict, 200)

    def patch(self, id):
        # Update an individual Order_product record by ID
        order_product = Order_product.query.filter_by(id=id).first()
        if not order_product:
            return make_response({"error": ["Order_product not found"]}, 404)
        try:
            for attr in request.json:
                setattr(order_product, attr, request.json[attr])
            db.session.add(order_product)
            db.session.commit()
            order_product_to_dict = order_product.to_dict()
            return make_response(order_product_to_dict, 202)
        except ValueError:
            return make_response({"errors": ["Validation errors"]}, 400)

    def delete(self, id):
        # Delete an individual Order_product record by ID
        order_product = Order_product.query.filter_by(id=id).first()
        if not order_product:
            return make_response({"error": ["Order_product not found"]}, 404)
        db.session.delete(order_product)
        db.session.commit()
        return make_response({}, 204)

api.add_resource(OrderProductsById, '/order_products/<int:id>')


class Reviews(Resource):
    def get(self):
        reviews = Review.query.all()
        reviews_list = [review.to_dict() for review in reviews]
        return make_response(reviews_list, 200)

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
        review_to_dict = review.to_dict()
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
            review_to_dict = review.to_dict()
            return make_response(review_to_dict, 202)
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





























if __name__ == '__main__':
    app.run(port=5555, debug=True)

