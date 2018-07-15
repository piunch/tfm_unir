var express = require('express');
var router = express.Router();
var Client = require('node-rest-client').Client;
const config = require('../config');

/* POST login details */
router.post('/', function(req, res, next) {
    user = req.body.user;
    pass = req.body.pass;

    var client = new Client();
    var args = {
        data: {
            "user": user,
            "password": pass
        },
        headers: { "Content-Type": "application/json" }
    };
    
    client.post(`http://${config.backend.host}:${config.backend.port}/v1/login`, args, function (data, response) {
        // parsed response body as js object
        res.cookie('apikey', JSON.stringify(data));
        res.send(JSON.stringify(data));
    });
});

module.exports = router;
