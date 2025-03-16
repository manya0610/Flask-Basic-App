from kombu import Queue, Exchange
from env import RMQ_BROKER_URL, RMQ_QUEUE, RMQ_EXCHANGE

broker_url = RMQ_BROKER_URL
queue = RMQ_QUEUE
exchange = RMQ_EXCHANGE

routing_key = "my-routing-key"
task_queues = (Queue(queue, Exchange(exchange), routing_key=routing_key),)

task_routes = {"src.celery_app.tasks.add": {"queue": queue},}


worker_hijack_root_logger = False
CELERYD_LOG_FILE = None
worker_redirect_stdouts = False
CELERYD_LOG_LEVEL = 'INFO'
