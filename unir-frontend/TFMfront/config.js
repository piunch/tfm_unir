const env = process.env.NODE_ENV;
const prodHost = process.env.PRO_HOST;

const test = {
    app: {
        port: 8081
    },
    backend: {
        host: '172.18.0.3',
        port: 8080
    }
};

const prod = {
    app: {
        port: 8080
    },
    backend: {
        host: prodHost,
        port: 8080
    }
};

const config = {
    test,
    prod
};

module.exports = config[env];