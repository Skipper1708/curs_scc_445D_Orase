#!/bin/sh
. .venv/bin/activate
export FLASK_APP=orase
flask run --host=0.0.0.0 --port=5011
