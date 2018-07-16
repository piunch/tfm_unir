FROM python:3.5-alpine

# Obtenemos por argumentos la clave del token y 
# los datos de conexión a BD
ARG TOKEN_KEY=tost4da
ARG BD_NAME=TFMUNIRBD
ARG BD_HOST
ARG BD_USER
ARG BD_PASSWORD

# Creamos el directorio donde poner el back
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
COPY test-requirements.txt /usr/src/app/

# Instalar requisitos de python
RUN pip3 install --no-cache-dir -r requirements.txt

# Copiar todos los fichero del back
COPY . /usr/src/app

# Generar el fichero de configuración
RUN printf "[AUTH]\n" > config.ini
RUN echo TOKEN_KEY = $TOKEN_KEY >> config.ini
RUN printf "\n[BBDD]\n" >> config.ini
RUN echo USER = $BD_USER >> config.ini
RUN echo PASSWORD = $BD_PASSWORD >> config.ini
RUN echo HOST = $BD_HOST >> config.ini
RUN echo DATABASE = $BD_NAME >> config.ini
# RUN cat config.ini

EXPOSE 8080

ENTRYPOINT ["python3"]
CMD ["-u", "-m", "swagger_server"]


# EJEMPLO DE USO
# docker build --build-arg TOKEN_KEY=***** --build-arg BD_HOST=**** --build-arg BD_USER=**** --build-arg BD_PASSWORD=**** -t tfmunirback .
# docker run -d --name=tfmunirback unir-back
