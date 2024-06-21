FROM langflowai/langflow:1.0-alpha

# Switch to root to install build tools and system dependencies
USER root

# Install build tools, Java, and required system libraries
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    poppler-utils \
    openjdk-17-jdk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME environment variable
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64
ENV PATH $JAVA_HOME/bin:$PATH

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
