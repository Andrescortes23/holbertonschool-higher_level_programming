#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let a;
  let ind = 0;
  for (a = 0; a < list.length; a++) {
    if (list[a] === searchElement) {
      ind++;
    }
  }
  return ind;
};
