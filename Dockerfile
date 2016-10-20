FROM ubuntu:14.04
MAINTAINER "Hoang Nam" <particle4dev@gmail.com>

RUN echo deb http://archive.ubuntu.com/ubuntu precise universe >> /etc/apt/sources.list
RUN apt-get update

# Install app dependencies
RUN apt-get install -qy libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev

## Python Family
RUN apt-get install -qy python-tk python python-dev python-distribute python-pip ipython

## Scrapy
RUN pip install lxml scrapy scrapyjs
RUN pip install --upgrade six
RUN pip install scrapyd-client

## Install Django
ADD ./requirements.txt /

RUN pip install -r /requirements.txt

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

EXPOSE 8000
EXPOSE 6800
