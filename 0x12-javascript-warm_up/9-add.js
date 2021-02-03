#!/usr/bin/node

const x = parseInt(process.argv[2]);
const y = parseInt(process.argv[3]);
function add (x, y) {
  return x + y;
}
console.log(parseInt(add(x, y)));
