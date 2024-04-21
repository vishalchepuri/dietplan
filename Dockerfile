FROM python:3.9-slim  


ARG API_KEY  
ENV API_KEY=$API_KEY  
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
EXPOSE 5000  
CMD ["python", "app.py","runserver"]  
