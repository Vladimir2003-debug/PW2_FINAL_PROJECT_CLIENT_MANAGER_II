FROM alpine

RUN apk update \
    && apk add . \
    && rm -rf /var/cache/apk/*

COPY ./manage.py /var/www/localhost/htdocs

CMD [".","-D","-f","/etc/PW2_FINAL_PROJECT_CLIENT_MANAGER/PW2_FINAL_PROJECT_CLIENT_MANAGER.conf"]