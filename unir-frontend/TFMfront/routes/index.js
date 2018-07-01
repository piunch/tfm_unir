var express = require('express');
var router = express.Router();

/* GET login page. */
router.get('/', function(req, res, next) {
  res.render('login', { title: 'Inicio de sesión' });
});

/* GET index page. */
router.get('/index', function(req, res, next) {
  res.render('index', { title: 'Inicio de sesión' });
});

module.exports = router;
