FROM node:8

EXPOSE 3000

CMD git clone https://github.com/piunch/tfm_unir.git && \
    cd tfm_unir && git checkout feature/front && \
    cd unir-frontend/TFMfront && npm install && \
    npm start