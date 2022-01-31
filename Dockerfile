FROM alpine:latest 

RUN apk add python3 py3-pip --no-cache
COPY . .
RUN pip install -r requirements.txt
CMD [ "python3", "./motd.py"]