<<<<<<< HEAD
# SAVIC OMS – Mini Order Fulfillment System (SAP-Inspired)

> A modern Order Management System inspired by the SAP Order-to-Cash (O2C) process, built using **React**, **FastAPI**, and **SQLite**.

---

## Project Overview

SAVIC OMS is a web-based Order Fulfillment System that simulates the initial stages of an enterprise Order-to-Cash (O2C) workflow.

The application enables customers to upload Purchase Orders, while suppliers review, validate, approve, reject, or partially approve them. Once approved, the system automatically generates Sales Orders and updates inventory accordingly.

The project is designed with a modular architecture and follows modern software engineering practices to demonstrate how enterprise order processing systems operate.

---

## Business Problem

Many organizations still process Purchase Orders manually through emails and spreadsheets.

This leads to:

* Manual inventory verification
* Duplicate Purchase Orders
* Data inconsistency
* Slow approval processes
* Poor visibility into order status
* Lack of centralized reporting

SAVIC OMS automates these processes using a centralized web application.

---

## Solution

The system provides:

* Role-based authentication
* Purchase Order upload
* Excel/PDF parsing
* Material validation
* Inventory validation
* Approval workflow
* Automatic Sales Order generation
* Inventory reservation
* Dashboard analytics
* Report generation

---

# Features

## Customer

* Login
* Upload Purchase Orders
* View Purchase Orders
* Track Order Status
* View Sales Orders
* View Order History

---

## Shopkeeper

* Login
* Review Purchase Orders
* Validate Inventory
* Approve Orders
* Reject Orders
* Partial Approval
* Generate Sales Orders
* Inventory Management
* Dashboard Analytics
* Export Reports

---

# Order Workflow

Customer Login

↓

Upload Purchase Order

↓

Document Processing

↓

Material Validation

↓

Inventory Validation

↓

Shopkeeper Review

↓

Approve / Reject / Partial Approval

↓

Sales Order Generation

↓

Inventory Update

↓

Customer Dashboard Updated

---

# Technology Stack

## Frontend

* React
* TypeScript
* Vite
* Tailwind CSS
* React Router
* TanStack Query
* Axios
* Recharts

---

## Backend

* FastAPI
* SQLAlchemy
* Alembic
* Pydantic
* JWT Authentication
* Pandas
* OpenPyXL
* pdfplumber

---

## Database

* SQLite

---

## Development Tools

* Git
* GitHub
* Docker
* Postman

---

# Architecture

The application follows a layered architecture.

```
React Frontend
        │
REST API
        │
FastAPI Backend
        │
Business Services
        │
Repository Layer
        │
SQLite Database
```

This separation improves maintainability, scalability, and testability.

---

# Project Structure

```
backend/
frontend/
docs/
uploads/
exports/
```

The backend follows a modular architecture using routers, services, repositories, models, and schemas.

---

# Database Modules

* Users
* Materials
* Inventory
* Purchase Orders
* Purchase Order Items
* Sales Orders

---

# User Roles

## Customer

Permissions:

* Upload Purchase Orders
* View Own Orders
* View Sales Orders
* View Order History

---

## Shopkeeper

Permissions:

* Review Orders
* Validate Inventory
* Approve Orders
* Reject Orders
* Generate Sales Orders
* View Inventory
* Export Reports

---

# Demo Credentials

## Customer

Username:

customer

Password:

Customer@123

---

## Shopkeeper

Username:

shopkeeper

Password:

Shopkeeper@123

---

# Installation

Clone the repository.

```
git clone <repository-url>
```

Backend

```
cd backend

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

alembic upgrade head

python seed/seed_data.py

uvicorn app.main:app --reload
```

Frontend

```
cd frontend

npm install

npm run dev
```

---

# API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI:

```
http://localhost:8000/docs
```

ReDoc:

```
http://localhost:8000/redoc
```

---

# Testing

The project includes tests for:

* Authentication
* Purchase Orders
* Inventory
* Sales Orders
* Validation Rules

Run:

```
pytest
```

---

# Documentation

Detailed documentation is available in the `docs/` directory.

* Requirement Analysis
* Architecture
* Database Design
* API Design
* Testing
* User Guide

---

# Future Enhancements

* PostgreSQL Support
* Redis Caching
* Email Notifications
* OCR for Scanned Purchase Orders
* Barcode Integration
* Multi-Warehouse Support
* AI Assistant
* SAP ERP Integration
* Role Management
* Audit Trail Enhancements

---

# Contributors

Developed as part of the SAVIC Internship Project.

---

# License

This project is developed for educational and internship purposes.
=======
# mini-order-fulfillment-system
 A modern Order Management System inspired by the SAP Order-to-Cash (O2C) process, built using **React**, **FastAPI**, and **SQLite**.
>>>>>>> a06c5e61b1458b89d99ee5bc8850bd6bda00cf80
