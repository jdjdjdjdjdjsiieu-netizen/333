FROM python:3.11-slim

WORKDIR /app

# Install build dependencies, if requirements.txt exists this will install them.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt || true

# Copy application code
COPY . .

ENV PYTHONUNBUFFERED=1

# Default command - adjust to your project's entrypoint (e.g. server, bot, etc.)
CMD ["python", "main.py"]