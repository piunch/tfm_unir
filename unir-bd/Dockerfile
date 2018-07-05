FROM mysql:5.7

ENV MYSQL_DATABASE=TFMUNIRBD
ENV MYSQL_USER=tfmunir
ENV MYSQL_PASSWORD=achusico123
ENV MYSQL_ROOT_PASSWORD=achusico.root.123

ADD config/bd_setup.sql /usr/src/sql/
ADD config/bd_setup.sh /usr/src/sql/
RUN ["chmod", "+x", "/usr/src/sql/bd_setup.sh"]
RUN ["chmod", "+x", "/usr/src/sql/bd_setup.sql"]

#ENTRYPOINT [" /usr/src/sql/bd_setup.sh"]

EXPOSE 3306

CMD /usr/src/sql/bd_setup.sh


# docker run --name=test-mysql mysql
# docker run --detach --name=test-mysql --env="MYSQL_ROOT_PASSWORD=achusico123" mysql