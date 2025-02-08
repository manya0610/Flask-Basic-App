from kombu import Queue, Exchange
import os


broker_url = "amqp://localhost:5672"
queue = "my-queue"
exchange = "my-exchange"

routing_key = "my-routing-key"
task_queues = (Queue(queue, Exchange(exchange), routing_key=routing_key), )

task_routes = {"celery_app.tasks.add" : {
    "queue" : queue
}}


worker_hijack_root_logger = False
CELERYD_LOG_FILE = None
worker_redirect_stdouts = False
