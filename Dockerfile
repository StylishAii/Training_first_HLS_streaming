FROM node:16-alpine as webapp

WORKDIR /apps

COPY /apps /apps
RUN yarn install --network-timeout 1000000
RUN yarn generate


FROM nginx:1.21.4 as production

COPY --from=webapp /apps/dist /usr/share/nginx/html

COPY config/nginx.conf /etc/nginx/nginx.conf
COPY config/mime.conf /etc/nginx/conf.d/mime.conf

EXPOSE 80