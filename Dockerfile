# Use an official Python 3.10 base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install dependencies directly in the container
RUN pip install --upgrade pip && \
    pip install --no-cache-dir pyswisseph==2.8.0.post1 && \
    pip install methodtools==0.4.7 && \
    pip install scipy==1.15.2 && \
    pip install astropy==6.1.7 && \
    pip install sanskrit_data==0.8.14 && \
    pip install indic-transliteration && \
    pip install curation_utils==0.2.10 && \
    pip install timebudget==0.7.1 && \
    pip install --no-deps jyotisha && \
    pip install "fastapi[standard]"

# Expose the FastAPI port
EXPOSE 8000

# Start FastAPI using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
