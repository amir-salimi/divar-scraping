FROM python:latest

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "migrate"]
cmd ["python" "manage.py" "makemigrations"]
# copy project
COPY . .


