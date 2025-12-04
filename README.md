# Employee Management API

A Django REST Framework-based backend for managing employees, their monthly lunch credit balances, and lunch orders.  
This project uses **SQLite (default database)** and includes **JWT authentication** and **Swagger API documentation**.

---

## 🚀 Tech Stack

- Python 3.10+
- Django 6
- Django REST Framework
- SQLite (Default DB)
- SimpleJWT (Access & Refresh Tokens)
- drf-yasg (Swagger / ReDoc)

---

## 📦 Setup Instructions

Follow these steps to run the project locally.

---

## Clone the Repository

```bash
git clone https://github.com/sankar-ak-eng/employee-management.git
cd employee-management
```
## Create & Activate Virtual Environment

# Windows
```bash
python -m venv venv
venv\Scripts\activate```

# Linux / Mac
```bash
python -m venv venv
venv\Scripts\activate```

# Windows
```bash
python -m venv venv
venv\Scripts\activate```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Apply Migrations (SQLite)

```bash
python manage.py makemigrations

python manage.py migrate

```
- SQLite DB file db.sqlite3 will be created automatically.

## Create Superuser

```bash 
python manage.py createsuperuser 
```
## Run Development Server


```bash
python manage.py runserver
```
[Swagger UI](http://127.0.0.1:8000/swagger/)
[Swagger JSON](http://127.0.0.1:8000/swagger.json)
[Swagger YAML](http://127.0.0.1:8000/swagger.yaml)
[ReDoc](http://127.0.0.1:8000/redoc/)


## JWT Authentication
# Get Tokens
POST /api/token/

Body:

```json
{
  "username": "admin",
  "password": "yourpassword"
}
```
# Refresh Token
POST /api/token/refresh/


## Project Structure
employee-management/
│
├── core/
│   ├── api/
│   │   └── v1/
│   ├── models/
│   ├── serializers/
│   ├── views/
│   ├── utils/
│   └── ...
│
├── lunch_credits/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── requirements.txt
├── manage.py
└── README.md

## Database (SQLite)

SQLite is the default development database.

Reset database
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```