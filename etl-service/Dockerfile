# 1. Use official lightweight Python image
FROM python:3.13-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy dependency file first (for better caching)
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application code
COPY etl.py .

# 6. Run the ETL script
CMD ["python", "etl.py"]