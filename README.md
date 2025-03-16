# Flask-Basic-App
To Create Migration
alembic revision --autogenerate -m "Create a baseline migrations"

To apply Migration
alembic upgrade head


To run celery app
celery -A src.celery_app worker -c 1 --loglevel=INFO