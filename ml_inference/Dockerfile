FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the download script to get the test data
RUN python download_data.py

# Make the shell script executable
RUN chmod +x run_inference.sh

# Run all inference scripts sequentially and print output
CMD ["sh", "run_inference.sh"]

