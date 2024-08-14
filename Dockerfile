# Import the needed base image for your app.
FROM python:slim

# Set the working directory to /app.
WORKDIR /app

# Copy the current directory contents into the container at /app.
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose the port that the application will listen on
EXPOSE 5000

# Run app.py when the container launches
CMD python ./app.py