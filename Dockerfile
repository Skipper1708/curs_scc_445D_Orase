FROM alpine:3.22

WORKDIR /app

RUN apk add --no-cache python3 py3-flask py3-pytest

COPY . /app

EXPOSE 5000

CMD ["python3", "orase.py"]
