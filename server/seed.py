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
        image_url="https://ibighit.com/bts/images/bts/discography/map_of_the_soul-7/img01.jpg",
        type='kpop'
    )
    kpop_merchandise.append(kpop_1)

    # Kpop Merchandise 2
    kpop_2 = Product(
        name="BLACKPINK - The Album",
        description="BLACKPINK's first full-length album with tracks like 'Lovesick Girls'.",
        price=29.99,
        release_date=date(2020 , 10 , 2),
        image_url="https://upload.wikimedia.org/wikipedia/en/f/f2/BLACKPINK-_The_Album.png",
        type='kpop'
    )
    kpop_merchandise.append(kpop_2)

    # Kpop Merchandise 3
    kpop_3 = Product(
        name="TWICE - Eyes Wide Open",
        description="TWICE's 2nd full album with the title track 'I Can't Stop Me'.",
        price=27.99,
        release_date=date(2020 , 10 ,26),
        image_url="https://upload.wikimedia.org/wikipedia/en/9/90/Twice_-_Eyes_Wide_Open.png",
        type='kpop'
    )
    kpop_merchandise.append(kpop_3)

    # Kpop Merchandise 4
    kpop_4 = Product(
        name="EXO - Don't Fight The Feeling",
        description="EXO's special album with a powerful title track of the same name.",
        price=23.99,
        release_date=date(2021, 6, 7),
        image_url="https://upload.wikimedia.org/wikipedia/en/5/5d/Exo_-_Don%27t_Fight_the_Feeling.png",
        type='kpop'
    )
    kpop_merchandise.append(kpop_4)

    # Kpop Merchandise 5
    kpop_5 = Product(
        name="IU - LILAC",
        description="IU's 5th studio album, a great addition to any Kpop collection.",
        price=24.99,
        release_date=date(2021, 3, 25),
        image_url="https://s3.amazonaws.com/thumbnails.thecrimson.com/photos/2021/04/05/201800_1349687.jpeg.1500x1500_q95_crop-smart_upscale.jpg",
        type='kpop'
    )
    kpop_merchandise.append(kpop_5)

    # Kpop Merchandise 6
    kpop_6 = Product(
        name="Stray Kids - IN生 (IN LIFE)",
        description="Stray Kids' repackaged album with tracks like 'Back Door'.",
        price=26.99,
        release_date=date(2020, 9 , 14),
        image_url="https://www.evepinkshop.com/cdn/shop/products/SKZ_9f6a8f1c-c8f7-4e21-83c6-321eb3b9a482_900x.jpg?v=1652395475",
        type='kpop'
    )
    kpop_merchandise.append(kpop_6)

    # Kpop Merchandise 7
    kpop_7 = Product(
        name="ATEEZ - ZERO : FEVER Part.2",
        description=" Idalis's Favorite Group; ATEEZ's 6th EP with hit songs like 'Fireworks (I'm The One)'.",
        price=22.99,
        release_date=date(2021, 3, 1),
        image_url="https://upload.wikimedia.org/wikipedia/en/thumb/5/50/Ateez_Fever_Part_2.jpg/220px-Ateez_Fever_Part_2.jpg",
        type='kpop'
    )
    kpop_merchandise.append(kpop_7)

    # Kpop Merchandise 8
    kpop_8 = Product(
        name="Mamamoo - Travel",
        description="Mamamoo's 10th mini-album featuring 'Aya & Dingga Dingga'.",
        price=19.99,
        release_date=date(2021, 11, 3),
        image_url="https://upload.wikimedia.org/wikipedia/en/6/65/Mamamoo_-_Travel.jpg",
        type='kpop'
    )
    kpop_merchandise.append(kpop_8)

    # Kpop Merchandise 9
    kpop_9 = Product(
        name="NCT 127 - Sticker",
        description="NCT 127's 3rd full-length album featuring the title track 'Sticker'.",
        price=27.99,
        release_date=date(2021, 9 , 17),
        image_url="https://upload.wikimedia.org/wikipedia/en/1/12/NCT_127_-_Sticker.png",
        type='kpop'
    )
    kpop_merchandise.append(kpop_9)

    # Kpop Merchandise 10
    kpop_10 = Product(
        name="GOT7 - Breath of Love: Last Piece",
        description="GOT7's 4th studio album with the title track 'Last Piece'.",
        price=25.99,
        release_date=date(2020 , 11, 30),
        image_url="https://upload.wikimedia.org/wikipedia/en/c/c6/BreathofLovecover.jpg",
        type='kpop'
    )
    kpop_merchandise.append(kpop_10)

    for kpop_item in kpop_merchandise:
        print(f"Adding K-Pop Product: {kpop_item.name} - Price: {kpop_item.price}")
        db.session.add(kpop_item)

    db.session.commit()
    return kpop_merchandise

def create_anime_merchandise():
    anime_merchandise = []

    # Anime Merchandise 1
    anime_1 = Product(
        name="One Piece Manga Volume 1",
        description="The first volume of the popular manga series One Piece by Eiichiro Oda.",
        price=12.99,
        release_date=date(1997, 12, 24),
        image_url="https://store.crunchyroll.com/on/demandware.static/-/Sites-crunchyroll-master-catalog/default/dwd48b860f/rightstuf/9781569319017_manga-One-Piece-Graphic-Novel-1-Romance-Dawn-East-Blue-primary.jpg",
        type='anime'
    )
    anime_merchandise.append(anime_1)

    # Anime Merchandise 2
    anime_2 = Product(
        name="Naruto Shippuden T-Shirt",
        description="A stylish t-shirt featuring characters from Naruto Shippuden anime.",
        price=19.99,
        release_date=date(2021, 5, 10),
        image_url="https://m.media-amazon.com/images/I/71d2M+WWDHL._AC_UY1000_.jpg",
        type='anime'
    )
    anime_merchandise.append(anime_2)

    # Anime Merchandise 3
    anime_3 = Product(
        name="My Neighbor Totoro Poster",
        description="An adorable poster of the iconic Studio Ghibli film My Neighbor Totoro.",
        price=8.99,
        release_date=date(1988, 4, 16),
        image_url="https://sothebys-md.brightspotcdn.com/dims4/default/d9297e0/2147483647/strip/true/crop/5154x7040+0+0/resize/800x1093!/quality/90/?url=http%3A%2F%2Fsothebys-brightspot.s3.amazonaws.com%2Fmedia-desk%2Fe1%2Fbe%2F0dc5489b41e0b9bb590b4421d75c%2Ftonari-no-totoro-my-neighbor-totoro-japanese-movie-poster.jpg",
        type='anime'
    )
    anime_merchandise.append(anime_3)

    # Anime Merchandise 4
    anime_4 = Product(
        name="Dragon Ball Z Goku Statue",
        description="A detailed statue of Goku from the Dragon Ball Z series.",
        price=39.99,
        release_date=date(2019 , 7 , 2),
        image_url="https://m.media-amazon.com/images/I/41tMO+4FY7L._AC_.jpg",
        type='anime'
    )
    anime_merchandise.append(anime_4)

    # Anime Merchandise 5
    anime_5 = Product(
        name="Attack on Titan Hoodie",
        description="A hoodie featuring the iconic Wings of Freedom symbol from Attack on Titan.",
        price=29.99,
        release_date=date(2020, 9 , 15),
        image_url="https://i.ebayimg.com/images/g/r3wAAOSwUOBdKRb~/s-l1200.webp",
        type='anime'
    )
    anime_merchandise.append(anime_5)

    # Anime Merchandise 6
    anime_6 = Product(
        name="Demon Slayer Pajama Set",
        description="A comfy pajama set with characters from the Demon Slayer anime.",
        price=32.99,
        release_date=date(2021, 12, 3),
        image_url="https://target.scene7.com/is/image/Target/GUEST_aaf97321-082b-4d0b-892c-91d7004a858b?wid=488&hei=488&fmt=pjpeg",
        type='anime'
    )
    anime_merchandise.append(anime_6)

    # Anime Merchandise 7
    anime_7 = Product(
        name="Sailor Moon Hat",
        description="A cute Sailor Moon-themed hat for all Sailor Scouts out there.",
        price=14.99,
        release_date=date(2020, 3 , 18),
        image_url="https://target.scene7.com/is/image/Target/GUEST_47aaca82-3895-4b95-9c8d-90ee8b9d189c?wid=488&hei=488&fmt=pjpeg",
        type='anime'
    )
    anime_merchandise.append(anime_7)

    # Anime Merchandise 8
    anime_8 = Product(
        name="Fullmetal Alchemist Figurine",
        description="A collectible figurine of Edward Elric from Fullmetal Alchemist.",
        price=27.99,
        release_date=date(2018, 11, 21),
        image_url="https://images.goodsmile.info/cgm/images/product/20200907/10021/74014/large/df88b824bc351e31dab4fdaae68a5e00.jpg",
        type='anime'
    )
    anime_merchandise.append(anime_8)

    # Anime Merchandise 9
    anime_9 = Product(
        name="Neon Genesis Evangelion Manga",
        description="The classic manga series Neon Genesis Evangelion by Yoshiyuki Sadamoto.",
        price=14.99,
        release_date=date(1995, 12, 23),
        image_url="https://m.media-amazon.com/images/I/81-uMgCK6zL._AC_UF1000,1000_QL80_.jpg",
        type='anime'
    )
    anime_merchandise.append(anime_9)

    # Anime Merchandise 10
    anime_10 = Product(
        name="One Punch Man Poster",
        description="A poster featuring Saitama from the popular anime One Punch Man.",
        price=7.99,
        release_date=date(2015, 4 ,9),
        image_url="https://m.media-amazon.com/images/I/717tGEHvPNL._AC_UF894,1000_QL80_.jpg",
        type='anime'
    )
    anime_merchandise.append(anime_10)

    for anime_item in anime_merchandise:
        db.session.add(anime_item)

    db.session.commit()
    return anime_merchandise





def create_orders(users, products):
    orders = []

    for _ in range(10):
        user = rc(users)
        status = rc(['In Progress', 'Completed', 'Cancelled', 'Shipped'])
        o = Order(user=user, status=status)
        db.session.add(o)
        
        # Commit the Order instance to get a valid ID
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error creating order: {str(e)}")

        for _ in range(randint(1, 5)):
            product = rc(products)
            if product.id is not None:
                op = Order_product(order_id=o.id, product_id=product.id)
                db.session.add(op)
            else:
                print(f"Invalid product ID: {product.id}")

        orders.append(o)

    db.session.commit()  # Commit once after all orders are added

    return orders

def create_reviews(users, products):
    reviews = []

    for _ in range(20):
        user = rc(users)
        product = rc(products)

        if user is not None and product is not None:
            review = Review(
                comments=fake.paragraph(),
                user=user,
                product=product
            )
            reviews.append(review)
        else:
            print(f"Invalid user or product: {user}, {product}")

    return reviews

if __name__ == '__main__':
    with app.app_context():
        print("Clearing the database...")
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
        # Commit once after all orders are added
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