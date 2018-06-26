var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
    //headers = req.header(sessionToken);
    res.render('index', { title: 'Inicio' });
});

module.exports = router;
