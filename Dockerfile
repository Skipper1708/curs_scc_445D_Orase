FROM alpine:3.19

RUN apk add --no-cache python3 py3-pip
RUN pip3 install flask --break-system-packages

WORKDIR /app
COPY . .

EXPOSE 5000
CMD ["python3", "orase.py"]
