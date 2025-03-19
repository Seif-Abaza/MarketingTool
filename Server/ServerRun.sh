#!/bin/bash
export FLASK_APP=Server/server.py
export FLASK_ENV=prodaction
export FLASK_DEBUG=0
export MT_DEBUG=0
# /opt/anaconda3/envs/Marketing/bin/python $FLASK_APP
flask run
