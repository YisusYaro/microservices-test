FROM python:3.9-alpine

WORKDIR /usr/src/app

COPY ./ /usr/src/app/

RUN apk add gcc musl-dev

RUN pip install pipenv

RUN pipenv install

CMD ["pipenv", "run", "start"]
