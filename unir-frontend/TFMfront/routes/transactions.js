var express = require('express');
var router = express.Router();
var Client = require('node-rest-client').Client;
const config = require('../config');

/* GET all transactions */
router.get('/', function(req, res, next) {
    authToken = req.cookies.apikey.replace(/\"/g,'');
    if (req.cookies.apikey == undefined) {
        res.sendStatuss(401);
        return;
    }

    var client = new Client();
    var args = {
        headers: { "api_key": authToken }
    };

    client.get(`http://${config.backend.host}:${config.backend.port}/v1/transaction`, args, function (data, response) {
        transactions = composeTransactions(data)
        res.send(transactions);
    });
});

/* GET account balance */
router.get('/balance', function(req, res, next) {
    authToken = req.cookies.apikey.replace(/\"/g,'');
    if (req.cookies.apikey == undefined) {
        res.sendStatuss(401);
        return;
    }

    var client = new Client();
    var args = {
        headers: { "api_key": authToken }
    };

    client.get(`http://${config.backend.host}:${config.backend.port}/v1/balance`, args, function (data, response) {
        res.send(JSON.stringify(data));
    });
});

/* POST transactions details */
router.post('/', function(req, res) {
    trxData = req.body;
    trxData.amount = Number(trxData.amount);
    authToken = req.cookies.apikey.replace(/\"/g,'');
    if (req.cookies.apikey == undefined) {
        res.sendStatuss(401);
        return;
    }

    var client = new Client();
    var args = {
        headers: { "api_key": authToken , 
                   "Content-Type": "application/json"
                },
        data: trxData
    };

    client.post(`http://${config.backend.host}:${config.backend.port}/v1/transaction`, args, function (data, response) {
        // parsed response body as js object
        res.status(response.statusCode).send(data);
    });
});

function composeTransactions(data) {
    transactions = [];
    for (let i = 0; i < data.length; i++) {
        trx = {};
        trx.x = data[i].transaction_date;
        trx.y = data[i].current_balance;
        transactions[i] = trx;
    }
    return transactions;
}



module.exports = router;
