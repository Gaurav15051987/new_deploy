FROM python:3.8
RUN pip install --upgrade pip
RUN mkdir /app
WORKDIR /app/
# Copy the rest of the codebase into the image
COPY . ./
COPY requirements.txt .

RUN pip install -r requirements.txt
CMD ["python", "./app.py"]