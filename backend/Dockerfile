FROM alpine:3.8

COPY . /usr/src
WORKDIR /usr/src

RUN apk add --no-cache python3 && \
    apk add --no-cache gcc && \
    apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev && \
    apk add --no-cache openssl-dev && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache && \
    ls && \
    pip3 install -r requirements.txt 

EXPOSE 22

CMD ["python3", "app.py"]