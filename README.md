Restaurant Management API

A production-ready REST API for managing restaurant menu, orders, and table bookings.
Includes JWT authentication, modular app structure, and Postman collection for testing.


1. Project Overview

This API provides backend functionality for a restaurant system:

User authentication (JWT)
Menu management (CRUD)
Order management (CRUD)
Booking management (CRUD)
Clean Django REST Framework architecture


2. Authentication (JWT) 
🔐Signup :  POST /api/accounts/signup/

Body:
{
  "username": "username",
  "password": "password"
}

Login (Get Tokens) : POST /api/accounts/token/

Refresh Token : POST /api/accounts/token/refresh/

🍛Menu API
Get All Menu Items : GET /api/menu/

Create Menu Item : POST /api/menu/

Body:
{
  "name": "Biriyani",
  "description": "Spicy dish",
  "price": 180,
  "category": "non-veg"
}

Update Menu Item : PUT /api/menu/<id>/

Delete Menu Item : DELETE /api/menu/<id>/

🛒Order API
Get All Orders : GET /api/orders/

Create an Order : POST /api/orders/

Retrieve One Order : GET /api/orders/<id>/

Update Order : PUT /api/orders/<id>/

Delete Order : DELETE /api/orders/<id>/

📅Booking API
Get All Bookings : GET /api/book/

Create Booking : POST /api/book/

Update Booking : PUT /api/book/<id>/

Delete Booking : DELETE /api/book/<id>/

3. Technologies Used

Python 3
Django
Django REST Framework
SimpleJWT
SQLite 
