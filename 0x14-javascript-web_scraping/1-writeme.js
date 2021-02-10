#!/usr/bin/node

const file = process.argv[2];
const towri = process.argv[3];
const fs = require('fs');
fs.writeFile(file, towri, (error) => {
  if (error) {
    console.log(error);
  }
});
