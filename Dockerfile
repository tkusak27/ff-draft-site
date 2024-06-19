# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install streamlit

# Make port 5000 available to the world outside this container
EXPOSE 8051/tcp

# Run app.py when the container launches
CMD ["streamlit", "run", "app/app.py", "--server.port", "8051"]