#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc
from datetime import datetime, timedelta

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db
from models import User, Order, Product, Order_product, Review

fake = Faker()

def create_users():
    users = []

    for _ in range(10):
        u = User(
            username = fake.name(),
            email = fake.email(),
            _password_hash= fake.password(length = 12)
        )
        users.append(u)
    return users



def create_products():
    products = []
    for _ in range(10):
        # Set the start date to January 1, 2000
        start_datetime = datetime(2000, 1, 1)

        # Set the end date to December 31, 2024
        end_datetime = datetime(2024, 12, 31)

        # Generate a random date within the specified date range
        random_date = fake.date_between(start_date=start_datetime, end_date=end_datetime)

        # Explicitly set the type to 'kpop' for Kpop products
        p = Product(
            name=fake.name(),
            description=fake.sentence(),
            price=randint(1, 50),
            release_date=random_date,  # Use the generated random date
            image_url=fake.image_url(),
            type='kpop'
        )
        products.append(p)

    for _ in range(10):
        # Set the start date to January 1, 2000
        start_datetime = datetime(2000, 1, 1)

        # Set the end date to December 31, 2024
        end_datetime = datetime(2024, 12, 31)

        # Generate a random date within the specified date range
        random_date = fake.date_between(start_date=start_datetime, end_date=end_datetime)

        # Explicitly set the type to 'anime' for Anime products
        p = Product(
            name=fake.name(),
            description=fake.sentence(),
            price=randint(1, 50),
            release_date=random_date,  # Use the generated random date
            image_url=fake.image_url(),
            type='anime'
        )
        products.append(p)

    return products




def create_orders(users, products):
    orders = []

    for _ in range(10):
        user = rc(users)
        o = Order(user=user)
        db.session.add(o)
        db.session.flush()

        for _ in range(randint(1, 5)):  # Each order can contain 1 to 5 products
            product = rc(products)
            op = Order_product(order=o, product=product)
            db.session.add(op)
        
        orders.append(o)
    
    return orders

def create_reviews(users, products):
    reviews = []

    for user in users:  # Create 20 random reviews
        product = rc(products)
        review = Review(
            comments=fake.paragraph(),  # Use paragraph() to generate longer comments
            user=user,
            product=product
        )
        reviews.append(review)
    
    return reviews

if __name__ == '__main__':
    with app.app_context():
        print("clearing the database...")
        db.drop_all()

        print("Creating tables...")
        db.create_all()

        print("Starting seed...")
        print("Seeding Users")
        seed_users = create_users()
        print("Seeding Products")
        seed_products = create_products()
        print("Seeding Orders")
        seed_orders = create_orders(seed_users, seed_products)
        print("Seeding Reviews")
        seed_reviews = create_reviews(seed_users, seed_products)

        db.session.add_all(seed_users)
        db.session.add_all(seed_products)
        db.session.add_all(seed_orders)
        db.session.add_all(seed_reviews)
        db.session.commit()
