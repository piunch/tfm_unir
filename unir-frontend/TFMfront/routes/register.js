var express = require('express');
var router = express.Router();
var Client = require('node-rest-client').Client;
const config = require('../config');

/* GET register page */
router.get('/', function(req, res, next) {
    //headers = req.header(sessionToken);
    res.render('register', { title: 'Inicio' });
});

/* POST register details */
router.post('/', function(req, res, next) {
    userData = req.body;
    
    var client = new Client();
    var args = {
        headers: { "Content-Type": "application/json" },
        data: userData
    };
    
    client.post(`http://${config.backend.host}:${config.backend.port}/v1/user`, args, function (data, response) {
        // parsed response body as js object
        console.log(response);
        res.status(response.statusCode).send(data);
    });
});

module.exports = router;
