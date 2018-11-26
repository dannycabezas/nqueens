FROM python:3

RUN mkdir /nqueensDocker

WORKDIR /nqueensDocker

COPY requirements.txt /nqueensDocker

RUN pip install -r requirements.txt

COPY . /nqueensDocker

CMD [ "python", "./main.py"]

