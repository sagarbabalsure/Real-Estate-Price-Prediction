FROM python:3.8.5-slim


#Working directory
WORKDIR /app

#install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

#copy source code
COPY /app .

EXPOSE 5000

#run application
CMD ["python","server.py"]