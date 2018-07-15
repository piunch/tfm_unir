var express = require('express');
var router = express.Router();
var jwt = require('jsonwebtoken');

/* GET login or index page. */
router.get('/', function(req, res, next) {
  if (req.cookies.apikey == undefined) {
    res.render('login', { title: 'Inicio de sesión' });
    return;
  }
  authToken = req.cookies.apikey.replace(/\"/g,'');

  authSecret = process.env.TOKEN_KEY;
  try {
    var decoded = jwt.verify(authToken, authSecret,  { algorithms: ['HS256'] });
  } catch(error) {
    res.render('login', { title: 'Inicio de sesión' });
    return;
  }
  res.render('index', { username: decoded.user });
});

module.exports = router;
