const env = process.env.NODE_ENV;

const test = {
    app: {
        port: 8080
    },
    backend: {
        host: '172.18.0.3',
        port: 8080
    }
};

const prod = {
    app: {
        port: 80
    },
    backend: {
        host: '',
        port: 8080
    }
};

const config = {
    test,
    prod
};

module.exports = config[env];