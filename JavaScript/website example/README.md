#Simple JS website

![unknown](https://user-images.githubusercontent.com/32592487/53598934-e8042200-3b9d-11e9-8622-6605ee82060c.png)

"""

var http = require('http');

var fs = require('fs');

"""

sets the variable "http" as the module "http"

sets the variable "fs" as the module "fs"

"""

http.createServer(function (request, response) {
  fs.readFile('demofile1.html', function(err, data) {
    response.writeHead(200, {'Content-Type': 'text/html'});
    response.write(data);
    response.end();
  });
}).listen(8080);

"""

this Creates the Web Server and sets the response as the contents of "demofile2.html"



