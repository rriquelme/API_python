FROM python:3.7-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY main.py ./
EXPOSE 8081
CMD ["python", "main.py"]
