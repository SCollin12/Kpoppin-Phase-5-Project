#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from models import User, Product, Order, Order_product, Review
from flask_restful import Api, Resource
from flask import Flask, make_response, jsonify, request, session
from flask_migrate import Migrate
from sqlalchemy.exc import SQLAlchemyError
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

            # Check if the username is already taken
            if User.query.filter_by(username=username).first():
                return {"errors": ["Username already taken"]}, 400

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

class UserDetails(Resource):
    def get(self, id):
        user = User.query.get(id)
        if not user:
            return make_response({"error": ["User not found"]}, 404)
        user_dict = user.to_dict(only=('id', 'username', 'email'))
        return make_response(user_dict, 200)

api.add_resource(UserDetails, '/users/<int:id>')


class Products(Resource):
    def get(self):
        products = [product.to_dict(only=('id', 'name', 'description', 'price', 'release_date', 'image_url', 'type')) for product in Product.query.all()]
        return make_response(products, 200)

    def post(self):
        try:
            data = request.json

            # Check if all required fields are present in the request data
            required_fields = ['name', 'description', 'price', 'release_date', 'image_url', 'type']
            for field in required_fields:
                if field not in data:
                    return {"errors": [f"Missing '{field}' field in the request data"]}, 400

            name = data['name']
            description = data['description']
            price = data['price']
            
            # Convert the release_date string to a Python date object
            release_date_str = data['release_date']
            release_date = parse(release_date_str).date()

            image_url = data['image_url']
            product_type = data['type']

            new_product = Product(
                name=name,
                description=description,
                price=price,
                release_date=release_date,
                image_url=image_url,
                type=product_type
            )

            db.session.add(new_product)
            db.session.commit()

            return make_response(new_product.to_dict(), 201)
        except KeyError as e:
            return {"errors": [f"KeyError: {str(e)} - Required field missing in the request data"]}, 400
        except Exception as e:
            return {"errors": [str(e)]}, 400

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
                if attr == 'release_date':
                    date_str = request.json[attr]
                    date_object = datetime.strptime(date_str, '%Y-%m-%d') # adjust the format as needed
                    setattr(product, attr, date_object)
                else:
                    setattr(product, attr, request.json[attr])
                
            db.session.add(product)
            db.session.commit()
            product_to_dict = product.to_dict(only = ('id', 'name', 'description', 'price', 'release_date', 'image_url', 'type'))
            return make_response(product_to_dict, 202)
        except ValueError as e:
            error_message = {"errors": ["Validation errors", str(e)]}
            return make_response(jsonify(error_message), 400)

    def delete(self, id):
        product = Product.query.filter_by(id=id).first()
        if not product:
            return make_response({"error": ["Product not found"]}, 404)
        db.session.delete(product)
        db.session.commit()
        return make_response({}, 204)

api.add_resource(ProductsById, '/products/<int:id>')

class ProductDetails(Resource):
    def get(self, id):
        product = Product.query.get(id)
        if not product:
            return make_response({"error": ["Product not found"]}, 404)
        product_dict = product.to_dict(only=('id', 'name', 'description', 'price', 'release_date', 'image_url', 'type'))
        return make_response(product_dict, 200)

api.add_resource(ProductDetails, '/products/<int:id>')


class Orders(Resource):
    def get(self):
        orders = [order.to_dict(only = ('id', 'user_id', 'status', 'order_products')) for order in Order.query.all()]
        return make_response(orders, 200)

    def post(self):
        try:
            user_id = request.json.get('user_id')
            product_ids = request.json.get('product_ids')

            if not user_id or not product_ids:
                return {"errors": ["Missing user_id or product_ids"]}, 400

            user = User.query.get(user_id)
            if not user:
                return {"errors": ["User not found"]}, 400

            new_order = Order(user_id=user_id)
            db.session.add(new_order)

            for product_id in product_ids:
                product = Product.query.get(product_id)
                if not product:
                    return {"errors": ["Product not found"]}, 400

                order_product = Order_product.query.filter_by(order_id=new_order.id, product_id=product_id).first()
                if not order_product:
                    new_order_product = Order_product(order_id=new_order.id, product_id=product_id)
                    db.session.add(new_order_product)

            db.session.commit()
            return make_response(new_order.to_dict(), 201)
        except Exception as e:
            return {"errors": [str(e)]}, 400
api.add_resource(Orders, '/orders')


class OrdersById(Resource):
    def get(self, id):
        order = Order.query.filter_by(id=id).first()
        if not order:
            return make_response({"error": ["Order not found"]}, 404)
        order_dict = order.to_dict()
        return make_response(order_dict, 200)

    def patch(self, id):
        order = Order.query.filter_by(id=id).first()
        if not order:
            return make_response({"error": ["Order not found"]}, 404)
        try:
            for attr in request.json:
                setattr(order, attr, request.json[attr])
            db.session.add(order)
            db.session.commit()
            return make_response(order.to_dict(only = ('id', 'user_id', 'status', 'order_products')), 202)
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
            order_id = request.json.get('order_id')
            product_id = request.json.get('product_id')

            if not order_id or not product_id:
                return {"errors": ["Missing order_id or product_id"]}, 400

            # Create the association between the order and the product
            new_order_product = OrderProduct(order_id=order_id, product_id=product_id)
            db.session.add(new_order_product)
            db.session.commit()
            return make_response(new_order_product.to_dict(), 201)
         except Exception as e:
            return {"errors": [str(e)]}, 400

api.add_resource(OrderProducts, '/order_products')


class OrderProductsById(Resource):
    def get(self, id):
        order_product = Order_product.query.filter_by(id=id).first()
        if not order_product:
            return make_response({"error": ["Order_product not found"]}, 404)
        order_product_dict = order_product.to_dict()
        return make_response(order_product_dict, 200)

    def patch(self, id):
        order_product = Order_product.query.filter_by(id=id).first()
        if not order_product:
            return make_response({"error": ["Order_product not found"]}, 404)
        try:
            for attr in request.json:
                setattr(order_product, attr, request.json[attr])
            db.session.add(order_product)
            db.session.commit()
            order_product_dict = order_product.to_dict()
            return make_response(order_product_dict, 202)
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
            comments = request.json['comments']
            user_id = request.json['user_id']
            product_id = request.json['product_id']

            # Check if the user and product actually exist in the database
            user = User.query.get(user_id)
            product = Product.query.get(product_id)

            if not user or not product:
                return {"errors": ["User or Product not found"]}, 400

            new_review = Review(
                comments=comments,
                user_id=user_id,
                product_id=product_id
            )

            db.session.add(new_review)
            db.session.commit()
            return make_response(new_review.to_dict(), 201)
        except Exception as e:
            return {"errors": [str(e)]}, 400

api.add_resource(Reviews, '/reviews')


class ReviewsById(Resource):
    def get(self, id):
        review = Review.query.filter_by(id=id).first()
        if not review:
            return make_response({"error": ["Review not found"]}, 404)
        review_dict = review.to_dict(only=('id', 'comments', 'user_id', 'product_id'))
        return make_response(review_dict, 200)

    def patch(self, id):
        review = Review.query.filter_by(id=id).first()
        if not review:
            return make_response({"error": ["Review not found"]}, 404)
        try:
            for attr in request.json:
                setattr(review, attr, request.json[attr])
            db.session.add(review)
            db.session.commit()
            review_dict = review.to_dict(only=('id', 'comments', 'user_id', 'product_id'))
            return make_response(review_dict, 202)
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

class ReviewsByProduct(Resource):
    def get(self, product_id):
        reviews = [review.to_dict(only=('id', 'comments', 'user_id', 'product_id'))
                   for review in Review.query.filter_by(product_id=product_id).all()]
        return make_response(reviews, 200)

api.add_resource(ReviewsByProduct, '/reviews/product/<int:product_id>')


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




























