# программа на основе которой будет создаваться наша программа
FROM python:latest
# создаётся директория
RUN mkdir /src
# перемещаемся в директорию src
WORKDIR /src
# копирует все файлы в текущей директории (.) и перемещает в src (/src)
COPY . /src
RUN pip install -r requirements.txt
