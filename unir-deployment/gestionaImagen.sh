#!/bin/bash

IMAGE = $0
IMAGE_FILE = $1

# Borramos los contenedores anteriores
if [ -n "$(docker container ls -a -q)" ]; then docker container rm -v -f $(docker container ls -a -q); fi

# Borramos la imagen anterior
if [ -n "$(docker images ${IMAGE} -q)" ]; then docker rmi -f $(docker images ${IMAGE} -q); fi
