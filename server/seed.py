#!/usr/bin/env python3


# Remote library imports
from faker import Faker  


# Standard library imports
from random import randint, choice as rc
from datetime import date

# Local imports
from app import app
from models import db
from models import User, Order, Product, Order_product, Review

from flask_bcrypt import Bcrypt


fake = Faker()


def create_users():
    users = []

    for _ in range(10):
        u = User(
            username = fake.name(),
            email = fake.email(),
            password_hash= fake.password(length=12)
        )
        users.append(u)
    return users


def create_kpop_merchandise():
    kpop_merchandise = []

    # Kpop Merchandise 1
    kpop_1 = Product(
        name="BTS - Map of the Soul: 7",
        description="BTS's 2020 album featuring hit songs like 'ON' and 'Black Swan'.",
        price=25.99,
        release_date=date(2020, 2 , 21),
        image_url="https://example.com/bts-map-of-the-soul-7.jpg",
        type='kpop'
    )
    kpop_merchandise.append(kpop_1)

    # Kpop Merchandise 2
    kpop_2 = Product(
        name="BLACKPINK - The Album",
        description="BLACKPINK's first full-length album with tracks like 'Lovesick Girls'.",
        price=29.99,
        release_date=date(2020 , 10 , 2),
        image_url="https://example.com/blackpink-the-album.jpg",
        type='kpop'
    )
    kpop_merchandise.append(kpop_2)

    # Kpop Merchandise 3
    kpop_3 = Product(
        name="TWICE - Eyes Wide Open",
        description="TWICE's 2nd full album with the title track 'I Can't Stop Me'.",
        price=27.99,
        release_date=date(2020 , 10 ,26),
        image_url="https://example.com/twice-eyes-wide-open.jpg",
        type='kpop'
    )
    kpop_merchandise.append(kpop_3)

    # Kpop Merchandise 4
    kpop_4 = Product(
        name="EXO - Don't Fight The Feeling",
        description="EXO's special album with a powerful title track of the same name.",
        price=23.99,
        release_date=date(2021, 6, 7),
        image_url="https://example.com/exo-dont-fight-the-feeling.jpg",
        type='kpop'
    )
    kpop_merchandise.append(kpop_4)

    # Kpop Merchandise 5
    kpop_5 = Product(
        name="IU - LILAC",
        description="IU's 5th studio album, a great addition to any Kpop collection.",
        price=24.99,
        release_date=date(2021, 3, 25),
        image_url="https://example.com/iu-lilac.jpg",
        type='kpop'
    )
    kpop_merchandise.append(kpop_5)

    # Kpop Merchandise 6
    kpop_6 = Product(
        name="Stray Kids - IN生 (IN LIFE)",
        description="Stray Kids' repackaged album with tracks like 'Back Door'.",
        price=26.99,
        release_date=date(2020, 9 , 14),
        image_url="https://example.com/stray-kids-in-life.jpg",
        type='kpop'
    )
    kpop_merchandise.append(kpop_6)

    # Kpop Merchandise 7
    kpop_7 = Product(
        name="ATEEZ - ZERO : FEVER Part.2",
        description=" Idalis's Favorite Group; ATEEZ's 6th EP with hit songs like 'Fireworks (I'm The One)'.",
        price=22.99,
        release_date=date(2021, 3, 1),
        image_url="https://example.com/ateez-zero-fever-part-2.jpg",
        type='kpop'
    )
    kpop_merchandise.append(kpop_7)

    # Kpop Merchandise 8
    kpop_8 = Product(
        name="Mamamoo - Travel",
        description="Mamamoo's 10th mini-album featuring 'Aya & Dingga Dingga'.",
        price=19.99,
        release_date=date(2021, 11, 3),
        image_url="https://example.com/mamamoo-travel.jpg",
        type='kpop'
    )
    kpop_merchandise.append(kpop_8)

    # Kpop Merchandise 9
    kpop_9 = Product(
        name="NCT 127 - Sticker",
        description="NCT 127's 3rd full-length album featuring the title track 'Sticker'.",
        price=27.99,
        release_date=date(2021, 9 , 17),
        image_url="https://example.com/nct-127-sticker.jpg",
        type='kpop'
    )
    kpop_merchandise.append(kpop_9)

    # Kpop Merchandise 10
    kpop_10 = Product(
        name="GOT7 - Breath of Love: Last Piece",
        description="GOT7's 4th studio album with the title track 'Last Piece'.",
        price=25.99,
        release_date=date(2020 , 11, 30),
        image_url="https://example.com/got7-last-piece.jpg",
        type='kpop'
    )
    kpop_merchandise.append(kpop_10)

    # for kpop_item in kpop_merchandise:
        # db.session.add(kpop_item)

    # db.session.commit()
    return kpop_merchandise

def create_anime_merchandise():
    anime_merchandise = []

    # Anime Merchandise 1
    anime_1 = Product(
        name="One Piece Manga Volume 1",
        description="The first volume of the popular manga series One Piece by Eiichiro Oda.",
        price=12.99,
        release_date=date(1997, 12, 24),
        image_url="https://example.com/one-piece-manga.jpg",
        type='anime'
    )
    anime_merchandise.append(anime_1)

    # Anime Merchandise 2
    anime_2 = Product(
        name="Naruto Shippuden T-Shirt",
        description="A stylish t-shirt featuring characters from Naruto Shippuden anime.",
        price=19.99,
        release_date=date(2021, 5, 10),
        image_url="https://example.com/naruto-tshirt.jpg",
        type='anime'
    )
    anime_merchandise.append(anime_2)

    # Anime Merchandise 3
    anime_3 = Product(
        name="My Neighbor Totoro Poster",
        description="An adorable poster of the iconic Studio Ghibli film My Neighbor Totoro.",
        price=8.99,
        release_date=date(1988, 4, 16),
        image_url="https://example.com/totoro-poster.jpg",
        type='anime'
    )
    anime_merchandise.append(anime_3)

    # Anime Merchandise 4
    anime_4 = Product(
        name="Dragon Ball Z Goku Statue",
        description="A detailed statue of Goku from the Dragon Ball Z series.",
        price=39.99,
        release_date=date(2019 , 7 , 2),
        image_url="https://example.com/goku-statue.jpg",
        type='anime'
    )
    anime_merchandise.append(anime_4)

    # Anime Merchandise 5
    anime_5 = Product(
        name="Attack on Titan Hoodie",
        description="A hoodie featuring the iconic Wings of Freedom symbol from Attack on Titan.",
        price=29.99,
        release_date=date(2020, 9 , 15),
        image_url="https://example.com/aot-hoodie.jpg",
        type='anime'
    )
    anime_merchandise.append(anime_5)

    # Anime Merchandise 6
    anime_6 = Product(
        name="Demon Slayer Pajama Set",
        description="A comfy pajama set with characters from the Demon Slayer anime.",
        price=32.99,
        release_date=date(2021, 12, 3),
        image_url="https://example.com/demon-slayer-pajama.jpg",
        type='anime'
    )
    anime_merchandise.append(anime_6)

    # Anime Merchandise 7
    anime_7 = Product(
        name="Sailor Moon Hat",
        description="A cute Sailor Moon-themed hat for all Sailor Scouts out there.",
        price=14.99,
        release_date=date(2020, 3 , 18),
        image_url="https://example.com/sailor-moon-hat.jpg",
        type='anime'
    )
    anime_merchandise.append(anime_7)

    # Anime Merchandise 8
    anime_8 = Product(
        name="Fullmetal Alchemist Figurine",
        description="A collectible figurine of Edward Elric from Fullmetal Alchemist.",
        price=27.99,
        release_date=date(2018, 11, 21),
        image_url="https://example.com/fma-figurine.jpg",
        type='anime'
    )
    anime_merchandise.append(anime_8)

    # Anime Merchandise 9
    anime_9 = Product(
        name="Neon Genesis Evangelion Manga",
        description="The classic manga series Neon Genesis Evangelion by Yoshiyuki Sadamoto.",
        price=14.99,
        release_date=date(1995, 12, 23),
        image_url="https://example.com/evangelion-manga.jpg",
        type='anime'
    )
    anime_merchandise.append(anime_9)

    # Anime Merchandise 10
    anime_10 = Product(
        name="One Punch Man Poster",
        description="A poster featuring Saitama from the popular anime One Punch Man.",
        price=7.99,
        release_date=date(2015, 4 ,9),
        image_url="https://example.com/one-punch-man-poster.jpg",
        type='anime'
    )
    anime_merchandise.append(anime_10)

    # for anime_item in anime_merchandise:
    #     db.session.add(anime_item)

    # db.session.commit()
    return anime_merchandise





def create_orders(users, products):
    orders = []

    for _ in range(10):
        user = rc(users)
        status = rc(['In Progress', 'Completed', 'Cancelled', 'Shipped'])
        o = Order(user=user, status=status)
        db.session.add(o)
        db.session.commit()  # Commit the Order instance to get a valid ID

        for _ in range(randint(1, 5)):  # Each order can contain 1 to 5 products
            product = rc(products)
            if product.id is not None:
                op = Order_product(order_id=o.id, product_id=product.id)
                db.session.add(op)
            else:
                print(f"Invalid product ID: {product.id}")

        orders.append(o)

    return orders

def create_reviews(users, products):
    reviews = []

    for _ in range(20):  
        user = rc(users)
        product = rc(products)
        review = Review(
            comments=fake.paragraph(),
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
        db.session.add_all(seed_users)
        db.session.commit()
        print("Seeding Products")
        seed_products = create_kpop_merchandise() + create_anime_merchandise()
        db.session.add_all(seed_products)
        db.session.commit()
        print("Seeding Orders")
        seed_orders = create_orders(seed_users, seed_products)
        db.session.add_all(seed_orders)
        db.session.commit()
        print("Seeding Reviews")
        seed_reviews = create_reviews(seed_users, seed_products)
        db.session.add_all(seed_reviews)
        db.session.commit()








# Here is the first version of the seed.py file 
#I had previously, 
#it ran and seeded without error:

# #!/usr/bin/env python3


# # Remote library imports
# from faker import Faker  # Import Faker


# # Standard library imports
# from random import randint, choice as rc
# from datetime import datetime, timedelta

# # Local imports
# from app import app
# from models import db
# from models import User, Order, Product, Order_product, Review

# from flask_bcrypt import Bcrypt

# # Create an instance of Faker
# fake = Faker()

# # Rest of your code...

# def create_users():
#     users = []

#     for _ in range(10):
#         u = User(
#             username = fake.name(),
#             email = fake.email(),
#             password_hash= fake.password(length=12)
#         )
#         users.append(u)
#     return users




# def create_products():
#     products = []
#     for _ in range(10):
#         # Set the start date to January 1, 2000
#         start_datetime = datetime(2000, 1, 1)

#         # Set the end date to December 31, 2024
#         end_datetime = datetime(2024, 12, 31)

#         # Generate a random date within the specified date range
#         random_date = fake.date_between(start_date=start_datetime, end_date=end_datetime)

#         # Explicitly set the type to 'kpop' for Kpop products
#         p = Product(
#             name=fake.name(),
#             description=fake.sentence(),
#             price=randint(1, 50),
#             release_date=random_date,  # Use the generated random date
#             image_url= fake.image_url(),
#             type='kpop'
#         )
#         products.append(p)

#     for _ in range(10):
#         # Set the start date to January 1, 2000
#         start_datetime = datetime(2000, 1, 1)

#         # Set the end date to December 31, 2024
#         end_datetime = datetime(2024, 12, 31)

#         # Generate a random date within the specified date range
#         random_date = fake.date_between(start_date=start_datetime, end_date=end_datetime)

#         # Explicitly set the type to 'anime' for Anime products
#         p = Product(
#             name=fake.name(),
#             description=fake.sentence(),
#             price=randint(1, 50),
#             release_date=random_date,  # Use the generated random date
#             image_url=fake.image_url(),
#             type='anime'
#         )
#         products.append(p)

#     return products




# def create_orders(users, products):
#     orders = []

#     for _ in range(10):
#         user = rc(users)
#         status = rc(['In Progress', 'Completed', 'Cancelled', 'Shipped'])
#         o = Order(user=user, status=status)
#         db.session.add(o)
#         db.session.flush()

#         for _ in range(randint(1, 5)):  # Each order can contain 1 to 5 products
#             product = rc(products)
#             op = Order_product(order=o, product=product)
#             db.session.add(op)
        
#         orders.append(o)
    
#     return orders

# def create_reviews(users, products):
#     reviews = []

#     for _ in range(20):  
#         user = rc(users)
#         product = rc(products)
#         review = Review(
#             comments=fake.paragraph(),
#             user=user,
#             product=product
#         )
#         reviews.append(review)

#     return reviews


# if __name__ == '__main__':
#     with app.app_context():
#         print("clearing the database...")
#         db.drop_all()

#         print("Creating tables...")
#         db.create_all()

#         print("Starting seed...")
#         print("Seeding Users")
#         seed_users = create_users()
#         print("Seeding Products")
#         seed_products = create_products()
#         print("Seeding Orders")
#         seed_orders = create_orders(seed_users, seed_products)
#         print("Seeding Reviews")
#         seed_reviews = create_reviews(seed_users, seed_products)

#         db.session.add_all(seed_users)
#         db.session.add_all(seed_products)
#         db.session.add_all(seed_orders)
#         db.session.add_all(seed_reviews)
#         db.session.commit()