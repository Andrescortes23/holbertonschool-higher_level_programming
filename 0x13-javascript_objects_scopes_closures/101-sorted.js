#!/usr/bin/node

const indata = require('./101-data').dict;
const outdata = {};
for (const a in indata) {
  if (outdata[indata[a]] === undefined) {
    outdata[indata[a]] = [];
  }
  outdata[indata[a]].push(a);
}
console.log(outdata);
