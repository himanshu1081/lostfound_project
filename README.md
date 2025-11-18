# Lost & Found (Django + Bootstrap)
Simple college project scaffold. No admin, minimal dependencies.

## Quick start
1. create virtualenv:
   ```bash
   python -m venv venv
   source venv/bin/activate   # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```
2. run migrations and start:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
3. open http://127.0.0.1:8000

## Structure
- accounts app: auth (register, login, logout)
- items app: LostItem, FoundItem, list/detail/add/resolve
- templates: bootstrap-based templates

