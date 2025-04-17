import logging
import re
import os
import gunicorn
wsgi_app = 'src.flask_server:create_app()'
bind = os.getenv("GUNICORN_HOST", "127.0.0.1") + ":" + os.getenv("GUNICORN_PORT", "5000")
workers = int(os.getenv("GUNICORN_WORKER_COUNT", 1)) # no of workers
threads = int(os.getenv("GUNICORN_THREAD_COUNT", 1)) # no of threads
timeout = int(os.getenv("GUNICORN_WORKER_TIMEOUT", 300)) # no of seconds
accesslog = '-'
filter_regex = r'/(static|_health)'
gunicorn.SERVER = 'MANYA'
# this filters out the routes which match the filter_regex
class RequestPathFilter(logging.Filter):
    def __init__(self, *args, path_re, **kwargs):
        super().__init__(*args, **kwargs)
        self.path_filter = re.compile(path_re)

    def filter(self, record):
        req_path = record.args['U']
        if self.path_filter.match(req_path):
            return False  # Don't log this entry
        # ... additional conditions can be added here ...
        return True     # Log this entry

def on_starting(server):
    server.log.access_log.addFilter(RequestPathFilter(path_re=filter_regex))