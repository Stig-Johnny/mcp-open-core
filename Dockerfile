# MCP Quantum Apex Sovereign Dockerfile

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy MCP Sovereign source code
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose API port
EXPOSE 5000

# Default sovereign execution command (entrypoint)
CMD ["python", "mcp_genesis.py"]
