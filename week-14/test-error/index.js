'use strict';

var fs = require('fs');
var createApp = require('./endpoint');

var app = createApp(fs);

app.listen(3000);
