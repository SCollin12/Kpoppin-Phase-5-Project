# Kpoppin-Phase-5-Project

## Description 
K-Poppin : Reloaded is an online K-Pop & Anime Merchandise store where users can create an account, browse inventory, add items to a cart, make purchases, and leave reviews.

## CRUD
C - Users create an account for website and write reviews for products and submit ratings.
R - Users should be able to view existing and ratings for products.
U - Users should be able to update their reviews, ratings, and items in cart.
D - Users should be able to delete their reviews and associated ratings.

## Wireframe
 ![image](https://github.com/SCollin12/Kpoppin-Phase-5-Project/assets/123848015/1d66bd88-46bb-488f-9c56-966e3ede41aa)

## Domain Model
  ![image](https://github.com/SCollin12/Kpoppin-Phase-5-Project/assets/123848015/8fb90e18-273b-4868-8631-c64d12e3725f)



## One-To/ Many-To-Many
A User can place many Orders, and an Order belongs to a single User.
A Product can be part of many Orders, and an Order can contain multiple Products.
A Product can belong to multiple Categories, and a Category can include multiple Products.
A User can leave multiple Reviews, and a Review is associated with a single User and a Single Product.
An Order can consist of multiple Products, and a Product can be part of multiple Orders through Order_Items.

## Validations
Username must exist.
Passwords must be at least 6 characters.
Cart must have at least one item to check out.
Review section must have at least 10 characters to submit.
