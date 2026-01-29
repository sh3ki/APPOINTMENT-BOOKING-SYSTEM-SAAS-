# Appointment & Booking System (SaaS)

Local-only full-stack setup with Django 5 + DRF + JWT + React 18.

## Backend Setup (Local)

1) Create and activate a virtual environment.
2) Install dependencies:

   - `pip install -r backend/requirements.txt`

3) Run migrations:

   - `python backend/manage.py migrate`

4) Create a superuser (optional):

   - `python backend/manage.py createsuperuser`

5) Start the backend:

   - `python backend/manage.py runserver`

API base: `http://localhost:8000/api`

## Frontend Setup (Local)

1) Install dependencies:

   - `npm install` (from `frontend`)

2) Start the app:

   - `npm start`

Frontend: `http://localhost:3000`

## Tests

Backend:
- `pytest` (from `backend`)

Frontend:
- `npm test` (from `frontend`)

## Environment Variables

Backend (optional):
- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `POSTGRES_NAME`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, `POSTGRES_PORT`
- `STRIPE_SECRET_KEY`, `PAYPAL_CLIENT_ID`, `PAYPAL_CLIENT_SECRET`
- `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_FROM_NUMBER`
- `DJANGO_EMAIL_BACKEND`, `DJANGO_EMAIL_HOST`, `DJANGO_EMAIL_HOST_USER`, `DJANGO_EMAIL_HOST_PASSWORD`

Frontend:
- `REACT_APP_API_URL` (defaults to `http://localhost:8000/api`)

## Notes

- SQLite is used by default for local development.
- PostgreSQL is supported by setting the `POSTGRES_*` environment variables.
- OAuth providers are configured via Django Allauth (Google/Apple).
- On Python 3.13, install a PostgreSQL driver separately if you need Postgres locally.
