#!/bin/bash

python3 -m gunicorn -c gunicorn.http.conf.py mock:mock &
python3 -m gunicorn -c gunicorn.https.conf.py mock:mock
