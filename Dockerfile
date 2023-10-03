# Use an official lightweight Python runtime as a parent image
FROM python:3.9-slim

# Create a non-root user and set the working directory
RUN useradd -m myuser
USER myuser
WORKDIR /home/myuser/app

# Copy only the requirements first to leverage Docker cache
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the desired port
EXPOSE 8081

# Command to run the Flask app
CMD ["python", "convert_to_jira.py"]
