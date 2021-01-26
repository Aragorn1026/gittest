FROM harbor-poc666.netease.com/zcq/centos7nginx:0.3

COPY ./nginx_start.sh /root/
RUN chmod +x /root/nginx_start.sh

EXPOSE 80/tcp 443/tcp

CMD ["/root/nginx_start.sh"]
