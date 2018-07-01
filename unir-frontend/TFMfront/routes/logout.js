var express = require('express');
var router = express.Router();

/* POST logout details */
router.post('/', function(req, res, next) {
    //headers = req.header(sessionToken);
    res.render('login', { title: 'Inicio' });
});

module.exports = router;
