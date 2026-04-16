FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/
COPY wait_for_services.sh .

RUN chmod +x wait_for_services.sh

CMD ["./wait_for_services.sh"]
