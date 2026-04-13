FROM nginx:stable
RUN rm -f /etc/nginx/conf.d/default.conf
COPY conf.default /etc/nginx/conf.d/default.conf
COPY html/ /usr/share/nginx/html/
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN chmod -R 755 /usr/share/nginx/html
EXPOSE 80
# CMD ["nginx","-g","daemon off;"]
CMD ["/entrypoint.sh"]
