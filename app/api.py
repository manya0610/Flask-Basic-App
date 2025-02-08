from flask import Blueprint, jsonify
from app import celery_app
from database.models import TestUser
from database import db_session
api = Blueprint('api', __name__)

@api.route('/api/hello', methods=['GET'])
def hello():
    celery_app.send_task("celery_app.tasks.add", args=[{"message": "boom"}])
    return jsonify(message="Hello, World!")


@api.route('/api/test', methods=['GET'])
def test():
    u = TestUser('admin1', 'admin@localhost1')
    db_session.add(u)
    db_session.commit()
    return jsonify(message="Hello, World!")