#!/usr/bin/node

const req = require('request');
let str = '';
const dc = {};

req(process.argv[2], function (error, stat, data) {
  if (error) {
    console.log(error);
  } else {
    str = JSON.parse(data);
    for (let a = 0; a < str.length; a++) {
      if (str[a].completed === true) {
        if (isNaN(dc[str[a].userId])) {
          dc[str[a].userId] = 0;
        }
        dc[str[a].userId] += 1;
      }
    }
  }
  console.log(dc);
});
