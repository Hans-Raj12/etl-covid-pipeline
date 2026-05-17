# start from official python image
from python:3.11-slim

# set working directory inside container
WORKDIR /app

# copy requirements first (for better caching)
COPY requirements.txt .

# install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

#copy all project files into container
COPY . .

RUN mkdir -p data

# command to run when contianer starts
CMD ["python", "main.py"]