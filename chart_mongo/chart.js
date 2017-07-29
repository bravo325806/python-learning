var koa = require('koa');
var app = koa();
var Router = require('koa-router');
var bodyparser = require('koa-bodyparser');
var chart = require('chart.js');
var views = require('co-views');
var serve = require('koa-static');
var server = require('http').createServer(app.callback());
var io = require('socket.io')(server);
var MongoClient = require('mongodb').MongoClient;
var ObjectId = require('mongodb').ObjectID;
var db;
MongoClient.connect("mongodb://localhost:27017/sensors", function (err, pDb) {
    if (err) {
        return console.dir(err);
    }
    db = pDb;
});
var server = require('http').createServer(app.callback());
var router = new Router();
const logger = require('koa-logger');

//mongo db data array
var currents = new Array();
var temp = new Array();
var humi = new Array();
var time = new Array();
var num = new Array();

function showdata() {
    var collection = db.collection('datas');
    collection.find({}).toArray(function (err, data) {
        for (var i = 0; i < data.length; i++) {
            currents[i] = data[i].Currents,
                temp[i] = data[i].Temperature,
                humi[i] = data[i].Humidity,
                time[i] = data[i].inserttime,
                num[i] = i;
            console.log('current: '+currents[i]);
            console.log('Temperature: '+temp[i]);
            console.log('Humidity: '+humi[i]);
            console.log('Inserttime: '+time[i]);
        }
    });
};

var render = views(__dirname, {
    map: {
        html: 'swig'
    }
});
app.use(bodyparser());
router.get('/', function* () {
    showdata();
    this.body = yield render("index", {
        "Currents": currents, //KEY:Currents ; Value:currents
        "Temperature": temp,
        "Humidity": humi,
        "Inserttime": time,
        "num": num
    });
});

router.post('/', function* () {

});

app.use(serve('./'));
app.use(router.middleware());
server.listen(3000, function () {
    console.log('listening on port 3000');
});