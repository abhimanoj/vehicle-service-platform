# Vehicle Service API

This Django REST Framework project provides APIs for managing vehicle-related information, users, and service orders.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django REST Framework

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/abhimanoj/vehicle-service-platform.git

## Navigate to the project folder:
    cd vehicle-service-api

2. **Install dependencies:**
    pip install -r requirements.txt

## Run migrations:
    python manage.py migrate

## Create a superuser:
    python manage.py createsuperuser

## Run the development server:
    python manage.py runserver

## Obtain Token
    curl -X POST -d "username=your_superuser_username&password=your_superuser_password" http://localhost:8000/api/token/

## Create Vehicle User:
    curl -X POST -H "Authorization: Token your_token_here" -d "fName=John&lname=Doe&email=test@gmail.com&phone=1234567890&status=Active&is_active=true" http://localhost:8000/api/vehicle-users/

## Get Vehicle Users:
    curl -H "Authorization: Token your_token_here" http://localhost:8000/api/vehicle-users/

## Get Single Vehicle User:
    curl -H "Authorization: Token your_token_here" http://localhost:8000/api/vehicle-users/1/

## Update Vehicle User:
    curl -X PATCH -H "Authorization: Token your_token_here" -d "fName=UpdatedName" http://localhost:8000/api/vehicle-users/1/

## Delete Vehicle User:
    curl -X DELETE -H "Authorization: Token your_token_here" http://localhost:8000/api/vehicle-users/1/

## Get Notifications: 
    curl -H "Authorization: Token your_token_here" http://localhost:8000/api/notifications/



