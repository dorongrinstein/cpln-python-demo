FROM python:3.10.2

WORKDIR /usr/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "example:app",  "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000
