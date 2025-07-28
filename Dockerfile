FROM python:3.10-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

RUN set -eux; \
    apt-get update && \
    apt-get install -y openjdk-17-jdk-headless
# Set the working directory in the container
WORKDIR /app

# Create a logs directory (as used by your script src/run_vinculados.py)
# This ensures the directory exists when the application tries to write logs.
RUN mkdir logs

# Copy the requirements file into the container
COPY requirements.txt .

# Copy the .env file into the container
COPY .env .

# Install Python dependencies
# Upgrade pip and then install packages from requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's source code into the container
# (respecting .dockerignore)
COPY . .

# Command to run your application
# CMD ["python3", "src/search_coords.py"]