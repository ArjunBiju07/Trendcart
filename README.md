TrendCart - E-commerce Platform

Overview
TrendCart is a full-stack e-commerce application built with Django and PostgreSQL. It provides a complete shopping experience for customers to browse products, manage shopping carts, and process orders while giving store managers powerful tools to manage inventory and sales.

Problem Statement

Online retail systems require:
- Efficient product catalog management
- Reliable shopping cart functionality
- Order history tracking
- Inventory management

Solution: A scalable e-commerce platform with role-based access control.

Key Features

For Customers:
- Browse product catalog with categories
- Add/remove items from shopping cart
- View total cart price in real-time
- View order history
- Track order status (Cart → Confirmed → Shipped)
- Secure user authentication
- Checkout functionality

For Store Managers/Admin:
- Add/Edit/Delete products
- Manage product categories
- Dynamic pricing management
- View customer orders
- Sales analytics dashboard
- Inventory tracking
- Admin dashboard interface

Tech Stack

-Frontend: Django Template Language, HTML/CSS 
-Backend: Python, Django (MVT Architecture) 
-Database: PostgreSQL 
-Authentication: Django Session Management 
-State Management: Database-backed Sessions 

Architecture

Django Apps:

-Products App: Manage product catalog and categories
-Customers App: Handle user profiles and accounts
-Orders App: Process orders and cart management
-Themes App: Dynamic frontend theming

