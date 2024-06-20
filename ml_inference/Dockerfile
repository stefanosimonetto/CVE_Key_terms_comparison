# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the download script to get the test data
RUN python download_data.py

# RUN all inferences for comparison
# Copy and run the shell script to execute all inference scripts
COPY run_inferences.sh /app/run_inferences.sh
RUN chmod +x /app/run_inferences.sh
CMD ["./run_inferences.sh"]