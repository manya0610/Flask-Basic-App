from typing import Any
from celery_app import celery_app


@celery_app.task(bind=True)
def add(_:Any, message:Any) -> dict[str, str]:
    print(message)
    for i in range(10):
        print(i)
    return {"message": "ok"}
