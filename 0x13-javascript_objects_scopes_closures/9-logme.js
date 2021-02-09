#!/usr/bin/node

let ind = 0;
exports.logMe = function (item) {
  console.log(ind + ': ' + item);
  ind += 1;
};
