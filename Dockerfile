FROM python:3.6-slim

RUN mkdir -p /var/www \
    && apt-get update \
    && apt-get install -y \
        build-essential \
        python-dev \
        git \
        python3-pip \
    && pip3 install -U pip
WORKDIR /var/www
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
ADD ./requirements.txt ./
ADD ./*.py ./
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD python ./main.py