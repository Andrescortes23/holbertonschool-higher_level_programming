#!/usr/bin/node

const req = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];
req(url, function (error, response, body) {
  if (error) { console.log(error); }
  fs.writeFile(file, body, 'utf-8', (err) => {
    if (err) { console.log(err); }
  });
});
