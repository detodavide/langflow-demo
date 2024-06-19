FROM langflowai/langflow:1.0-alpha

# Switch to root to install build tools
USER root

# Install build tools
RUN apt-get update && apt-get install -y build-essential

# Copy requirements file
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Switch back to the non-root user
USER user

# Set the working directory
WORKDIR /app

# Set the entrypoint for the container
ENTRYPOINT ["python", "-m", "langflow", "run"]

# Set the default command-line arguments for the entrypoint
CMD ["--host", "0.0.0.0", "--port", "7860"]
