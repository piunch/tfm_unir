var express = require('express');
var router = express.Router();

/* POST login details */
router.post('/', function(req, res, next) {
    //headers = req.header(sessionToken);
    res.render('index', { title: 'Inicio' });
});

module.exports = router;
