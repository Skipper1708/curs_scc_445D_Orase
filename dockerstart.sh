#!/bin/sh

. .venv/bin/activate

export FLASK_APP=orase

cale=$(pwd)
echo "Directorul curent: $cale"
ls -la

flask run --host=0.0.0.0 --port=5011
