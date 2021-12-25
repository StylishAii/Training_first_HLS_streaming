FROM nginx:1.21.4
COPY config/nginx.conf /etc/nginx/nginx.conf
COPY config/mime.conf /etc/nginx/conf.d/mime.conf