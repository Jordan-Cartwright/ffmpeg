FROM alpine:3.10
LABEL maintainer="Jordan-Cartwright"

# Environment variables for localization
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

# Debugging
ARG DEBUGGING=false
ENV DEBUGGING=$DEBUGGING

# Add pip requirements
COPY requirements.txt /tmp/requirements.txt

# Install needed Packages
RUN apk update \
 && apk add --no-cache \
        python3 \
        ffmpeg \
 && python3 -m pip install --no-cache-dir -r /tmp/requirements.txt  \
 && rm -rf /tmp/* /var/tmp/*

# Copy Project Files, needs to be more selective
COPY / /app/

RUN addgroup -S unmanic && adduser -S -g unmanic unmanic \
    # For Cache, Code, Configs, and Library Files
    && mkdir -p /tmp/unmanic /app /config/ /library \
    && chown -R unmanic /tmp/unmanic /app /config/ /library && chgrp -R unmanic /tmp/unmanic /app /config/ /library

EXPOSE 8888

# Needed to be set since paths in python code aren't handled properly
WORKDIR /app

# Set User to Unmanic
USER unmanic

CMD ["/usr/bin/python3", "-u" , "/app/service.py"]
