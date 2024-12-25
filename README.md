# Car Rental Website

A full-stack web application for renting cars and allowing users to list their vehicles for rent. Built with Django, React, and MySQL.

## Features

- Users can browse available cars and view details like model, rent price, and owner information.
- Car owners can list their cars for rent with specifications and pricing.
- Secure user authentication and profile management.
- Dynamic and responsive user interface.
- Data persistence using MySQL database.

## Technologies Used

### Frontend:
- **React**: For building the user interface.
- **Axios**: For making API requests.
- **CSS**: For styling the application.

### Backend:
- **Django**: For building RESTful APIs and managing server-side logic.
- **Django REST Framework**: For API development.

### Database:
- **MySQL**: For storing user, car, and rental data.


## Installation and Setup

Follow these steps to set up the project locally:

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Node.js and npm
- MySQL

### Backend Setup (Django)
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/car-rental-website.git
   cd car-rental-website/backend


2. Create and activate a virtual environment:
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:

bash
pip install -r requirements.txt

4. Configure MySQL database in settings.py:

python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

5. Run migrations:

bash
python manage.py makemigrations
python manage.py migrate

6. Start the server:

bash
python manage.py runserver

7. Navigate to the frontend directory:

bash
cd ../frontend

8. Install dependencies:

bash
npm install

9. Start the React development server:

bash
npm start


Ensure the frontend is correctly configured to interact with the backend API. Update the API base URL in your React project.
