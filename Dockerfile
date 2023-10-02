# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install libpq-dev without using sudo
RUN apt-get update && apt-get install -y libpq-dev

# Install psycopg2-binary instead of psycopg2
RUN pip install --no-cache-dir psycopg2-binary

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8000

# Define environment variable
#ENV NAME World

# Run app.py when the container launches
CMD ["uvicorn", "project:app", "--reload", "--host", "0.0.0.0"]

