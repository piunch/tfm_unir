#!/bin/bash
set -e
service mysql start

echo "Generando BD..."
mysql < /usr/src/sql/bd_setup.sql

echo "Creando usuario para la BD..."
mysql -e "CREATE USER '${MYSQL_USER}' IDENTIFIED BY '${MYSQL_PASSWORD}';"
mysql -e "GRANT ALL PRIVILEGES ON TFMUNIRBD.* TO '${MYSQL_USER}'@'%'; FLUSH PRIVILEGES;"

echo "[Terminado]"
mysql