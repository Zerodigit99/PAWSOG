# Use the Python 3.10.11 image with Alpine 3.18
FROM python:3.10.11-alpine3.18

# Install necessary dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev python3-dev openssl-dev

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Create a directory for session files if needed
RUN mkdir -p sessions

# Set environment variables
ENV PYTHONIOENCODING=utf-8
ENV TERM=xterm-256color

# Copy the run.sh script
COPY run.sh ./
RUN chmod +x run.sh  # Make the script executable

# Start the application using the run.sh script
CMD ["./run.sh"]