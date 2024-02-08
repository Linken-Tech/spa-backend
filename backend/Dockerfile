FROM python:3.9-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app/api
COPY requirements.txt /app/api
RUN pip install -r requirements.txt
COPY . /app/api
RUN chmod +x entrypoint.sh
EXPOSE 8000
