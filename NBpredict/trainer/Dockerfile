FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY . /app

RUN pip install --no-cache-dir numpy python-dateutil pytz
RUN pip install --no-cache-dir pandas

CMD ["python", "trainer.py"]
FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY . /app

RUN pip install --no-cache-dir numpy python-dateutil pytz
RUN pip install --no-cache-dir pandas

CMD ["python", "trainer.py"]
