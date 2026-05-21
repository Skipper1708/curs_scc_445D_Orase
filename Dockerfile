FROM python:3.10-alpine

ENV FLASK_APP=orase

RUN adduser -D orase

COPY dockerstart.sh /home/orase/dockerstart.sh
RUN chmod +x /home/orase/dockerstart.sh

USER orase
WORKDIR /home/orase/

COPY app app
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY orase.py orase.py

RUN python3 -m venv .venv
RUN .venv/bin/pip install -r quickrequirements.txt

EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
