from src.celery_app import celery_app


@celery_app.task(bind=True)
def add(self, message) -> dict[str, str]:
    print(self, message)
    for i in range(10):
        print(i)
    return {"message": "ok"}
