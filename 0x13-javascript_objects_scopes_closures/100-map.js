#!/usr/bin/node

const list = require('./100-data.js').list;
const listn = list.map((item, i) => item * i);
console.log(list);
console.log(listn);
