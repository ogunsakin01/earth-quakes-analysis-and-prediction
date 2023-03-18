# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt
# Copy the rest of the application code into the container
COPY . .

# Expose port 80 for the API
EXPOSE 80

# Start the API when the container launches
CMD ["python", "main.py"]
