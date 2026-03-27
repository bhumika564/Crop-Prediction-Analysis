# Stage 1: Base Image
# Python 3.10 ka slim version use kar rahe hain for smaller image size
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# 1. Copy dependencies file first to leverage Docker layer caching
COPY requirements.txt .

# 2. Install Python dependencies using the requirements file
RUN pip install --no-cache-dir -r requirements.txt --default-timeout=100

# 3. Copy ALL application code and the ML model files
# Yeh . (dot) is current (backend) directory ke saare contents ko container ke /app mein copy karega.
# Ismein aapka app.py, models folder, data folder, aur utils folder sab aa jayenge.
COPY . .

# 4. Expose the port (Flask default is usually 5000)
EXPOSE 5000

# 5. Define the command to run the Flask application when container starts
CMD ["python", "app.py"]