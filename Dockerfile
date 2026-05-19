FROM python:3.10-alpine

WORKDIR /home/orase

COPY app app
COPY orase.py orase.py
COPY quickrequirements.txt quickrequirements.txt
COPY pytest.ini pytest.ini

RUN python3 -m venv .venv
RUN .venv/bin/pip install --no-cache-dir -r quickrequirements.txt

EXPOSE 5011

CMD [".venv/bin/python", "orase.py"]
