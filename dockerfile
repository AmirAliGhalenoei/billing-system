FROM python:3.11.15-trixie

LABEL Project_Name="Billing-system"

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY  requirements.txt /app/
RUN pip install -U pip -i https://mirror.abrha.net/repository/pypi/simple
RUN pip install -r requirements.txt -i https://mirror.abrha.net/repository/pypi/simple

COPY . /app/

EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
