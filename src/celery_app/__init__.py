from celery import Celery

celery_app = Celery("src.celery_app", include=["src.celery_app.tasks"])
celery_app.config_from_object("configs.celeryconfig")
