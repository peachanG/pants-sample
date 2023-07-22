FROM ubuntu:18.04

ARG PYTHON_VERSION=3.8
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y software-properties-common

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update && \
    apt-get install -y python${PYTHON_VERSION} python${PYTHON_VERSION}-dev python3-pip python3-setuptools

RUN rm -f /usr/bin/python && \
    rm -f /usr/bin/python3 && \
    ln -s /usr/bin/python${PYTHON_VERSION} /usr/bin/python3 && \
    ln -s /usr/bin/python3 /usr/bin/python

# update pip
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN ln -s /usr/bin/pip3 /usr/bin/pip

ENTRYPOINT ["/bin/whisper"]
COPY src.python.main.whisper/main.pex /bin/whisper