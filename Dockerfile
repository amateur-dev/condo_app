FROM python:latest
WORKDIR /home
COPY . .
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get upgrade -y
# RUN apt-get install postgres
RUN apt-get install sudo
RUN alias pip=pip3
RUN alias python=python3
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
CMD tail -f /dev/null