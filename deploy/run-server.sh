#!/bin/bash

echo $GUNICORN_PORT
python3 -m gunicorn -c configs/gunicorn.conf.py