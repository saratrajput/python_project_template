# Base image
FROM ubuntu:20.04

ENV HOME /home
ENV DEBIAN_FRONTEND=noninteractive

# Install required packages
RUN apt-get update && apt-get -y --no-install-recommends install \
    python3 \
    python3-pip \
    git \
    ffmpeg \
    libsm6 \
    libxext6

# Copy files
COPY . /home/

# Install dependencies
RUN pip install -r /home/requirements.txt

ENV TERM=xterm
