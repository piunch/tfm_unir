var express = require('express');
var router = express.Router();

/* GET all transactions */
router.get('/', function(req, res, next) {

});

/* POST transactions details */
router.post('/', function(req, res) {
    console.log(req.body)
    // var client = new Client();
    // var args = {
    //     data: { : "" },
    //     headers: { "Content-Type": "multipart/form-data" }
    // };
    res.send("kkfuti")
});

module.exports = router;
