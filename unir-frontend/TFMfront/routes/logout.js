var express = require('express');
var router = express.Router();
var Client = require('node-rest-client').Client;

/* POST logout details */
router.get('/', function(req, res, next) {
    authToken = req.cookies.apikey.replace(/\"/g,'');
    
    var client = new Client();
    var args = {
        headers: { "api_key": authToken }
    };
    client.delete("http://localhost:8080/v1/logout", args, function (data, response) {
        if (response.statusCode == 200) {
            res.clearCookie("apikey");
            res.redirect('/');
        }
    });
});

module.exports = router;
