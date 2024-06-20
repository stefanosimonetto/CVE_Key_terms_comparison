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
RUN python main_comparison\cve_all_terms\inference.py
RUN python main_comparison\cve_core\inference.py
RUN python main_comparison\cve_core_consequences\inference.py
RUN python main_comparison\cve_core_contextual\inference.py
RUN python main_comparison\cve_descr_repl_subj\inference.py
RUN python main_comparison\cve_description\inference.py

# RUN comparison between bert and phi
RUN python bert_phi_comparison\bert\inference.py
RUN python bert_phi_comparison\phi\inference.py




# Run all inference scripts sequentially and print output
CMD ["sh", "-c", "python main_comparison\cve_all_terms\inference.py && python inference_2.py && python inference_3.py && python inference_4.py && python inference_5.py && python inference_6.py && python inference_7.py && python inference_8.py && python inference_9.py"]