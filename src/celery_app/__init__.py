from celery import Celery


celery_app = Celery("celery_app.tasks")
celery_app.config_from_object("configs.celeryconfig")
