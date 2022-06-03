FROM node:16.15.0-alpine3.15

RUN apk add --no-cache nano bash g++ gcc libgcc libstdc++ linux-headers make yarn

ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000

COPY . .

WORKDIR /usr/src/app/bank_django_nuxt3_frontend

EXPOSE 3000

ENTRYPOINT ["./.docker/entrypoint.sh"]