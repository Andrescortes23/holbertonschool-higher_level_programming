#!/usr/bin/node

const file = process.argv;
const fs = require('fs');
fs.readFile(file[2], 'utf-8', (err, data) => {
  if (err) { console.log(err); }
  console.log(data);
});
