FROM python:3.9-alpine
WORKDIR /opt/sohei
COPY . .
RUN apk add build-base
RUN python3 -m pip install -r requirements.txt
ENTRYPOINT ['/opt/sohei/docker-entrypoint.sh']
