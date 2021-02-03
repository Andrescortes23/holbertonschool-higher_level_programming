#!/usr/bin/node

const val = parseInt(process.arg[2]);
if (isNaN(val) === true) {
  console.log('Not a number');
} else {
  console.log('My number:', val);
}
