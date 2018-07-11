FROM mysql:5.7

ARG MYSQL_DATABASE=TFMUNIRBD
ARG MYSQL_USER
ARG MYSQL_PASSWORD
ARG MYSQL_ROOT_PASSWORD

ENV MYSQL_DATABASE=$MYSQL_DATABASE
ENV MYSQL_USER=$MYSQL_USER
ENV MYSQL_PASSWORD=$MYSQL_PASSWORD
ENV MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD

ADD config/bd_setup.sql /usr/src/sql/
ADD config/bd_setup.sh /usr/src/sql/
RUN ["chmod", "+x", "/usr/src/sql/bd_setup.sh"]
RUN ["chmod", "+x", "/usr/src/sql/bd_setup.sql"]

#ENTRYPOINT [" /usr/src/sql/bd_setup.sh"]

EXPOSE 3306

CMD /usr/src/sql/bd_setup.sh


# docker run --name=test-mysql mysql
# docker build --build-arg MYSQL_USER=***** --build-arg MYSQL_PASSWORD=***** --build-arg MYSQL_ROOT_PASSWORD=***** -t bd .
# docker run -dt --name=test-mysql --env="MYSQL_ROOT_PASSWORD=achusico123" mysql