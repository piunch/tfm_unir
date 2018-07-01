var express = require('express');
var router = express.Router();

/* GET register page */
router.get('/', function(req, res, next) {
    //headers = req.header(sessionToken);
    res.render('index', { title: 'Inicio' });
});

/* POST register details */
router.post('/', function(req, res, next) {
    res.render('index', { title: 'Inicio' });
});

module.exports = router;
