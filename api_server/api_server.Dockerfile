FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc

# Install dependencies
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
