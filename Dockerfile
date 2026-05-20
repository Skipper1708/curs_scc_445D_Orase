FROM python:3.10-alpine

ENV FLASK_APP=orase

RUN adduser -D orase
USER orase
WORKDIR /home/orase/

COPY app app
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY orase.py orase.py

RUN python3 -m venv .venv
RUN .venv/bin/pip install -r quickrequirements.txt
RUN chmod +x dockerstart.sh

EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
