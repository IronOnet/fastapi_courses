FROM python:30.10-alpine 

# Set the working directory in the container 
WORKDIR /app 

# Copy the requirments file to the container 
COPY requirments.txt .  

# INSTALL the project dependencies 
RUN pip install --no-cache-dir -r requirements.txt 

# Copy the project files to the container 
COPY . . 

# Expose the port on which the FastAPI server will run 
EXPOSE 8000 

# Start the FastAPI server 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]