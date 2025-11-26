# Django from Scratch

A personal learning project to understand and develop web applications using Django, a powerful and versatile Python web framework.

## Overview

This repository contains my journey through learning Django, from fundamental concepts to building complete web applications.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

### How I created this repo

These are the instructions step by step:
```bash
mkdir django-course
cd django-course
python3 -m venv .venv
source .venv/bin/activate
pip install Django
pip freeze > requirements.txt
django-admin startproject mysite
nano mysite/mysite/settings.py # and edit line 28 -> ALLOWED_HOSTS = ['*']
cd mysite
python manage.py startapp polls 
python manage.py check
python polls/create-polls-models.py # creates some fixtures
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/django-course.git
cd django-course
```

2. Create and activate a virtual environment:
```bash
python3 -m venv .venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create a superuser (for admin access):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Project Structure

```
django-course/
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── [project-name]/       # Main project directory
    ├── settings.py       # Project settings
    ├── urls.py          # URL routing
    ├── wsgi.py          # WSGI configuration
    ├── asgi.py          # ASGI configuration
    └── [app-name]/      # Django applications
        ├── models.py    # Database models
        ├── views.py     # View logic
        ├── urls.py      # App URL routing
        ├── admin.py     # Admin configuration
        ├── tests.py     # Tests
        └── templates/   # HTML templates
```

## Learning Topics

This project covers:

- [ ] Django setup and configuration
- [ ] Models and database design
- [ ] Views and URL routing
- [ ] Templates and template tags
- [ ] Forms and validation
- [ ] Static files and media
- [ ] User authentication
- [ ] Class-based views
- [ ] Django ORM queries
- [ ] Admin interface
- [ ] Middleware
- [ ] Signals
- [ ] Testing
- [ ] Deployment basics

## Useful Commands

```bash
# Create a new app
python manage.py startapp appname

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Access the shell
python manage.py shell

# Run tests
python manage.py test

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Start development server
python manage.py runserver
```

## Resources

Django official tutorial -> https://docs.djangoproject.com/en/5.2/intro/tutorial01/
Django freeCodeCamp full course -> https://www.youtube.com/watch?v=o0XbHvKxw7Y

## License

This project is created for educational purposes.
