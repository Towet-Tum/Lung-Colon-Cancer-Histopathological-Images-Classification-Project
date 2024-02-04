# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt

RUN pip install -r requirements.txt

# Expose port 8000 for the Django app to run on
EXPOSE 8000

# Run Django migrations and collect static files
RUN python LungColonClassification/manage.py migrate
RUN python LungColonClassification/manage.py collectstatic --noinput

# Start the Django app
CMD ["python", "LungColonClassification/manage.py", "runserver", "0.0.0.0:8000"]