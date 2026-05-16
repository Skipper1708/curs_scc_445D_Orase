FROM alpine

RUN apk add --no-cache python3 py3-pip

RUN adduser -D orase
USER orase
WORKDIR /home/orase/

COPY --chown=orase app app
COPY --chown=orase orase.py orase.py
COPY --chown=orase quickrequirements.txt quickrequirements.txt
COPY --chown=orase pytest.ini pytest.ini

RUN python3 -m venv .venv
RUN .venv/bin/pip install --no-cache-dir -r quickrequirements.txt

EXPOSE 5011

CMD [".venv/bin/python", "orase.py"]
