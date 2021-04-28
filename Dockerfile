FROM python:3-alpine

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .

EXPOSE 80/tcp
LABEL ApiServiceName="service-test"

CMD [ "python", "./server.py"]