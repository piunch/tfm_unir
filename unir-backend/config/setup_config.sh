printf "[AUTH]\n" > config.ini
echo TOKEN_KEY = $TOKEN_KEY >> config.ini
printf "\n[BBDD]\n" >> config.ini
echo USER = $BD_USER >> config.ini
echo PASSWORD = $BD_PASSWORD >> config.ini
echo HOST = $BD_HOST >> config.ini
echo DATABASE = $BD_NAME >> config.ini

python3 -u -m swagger_server