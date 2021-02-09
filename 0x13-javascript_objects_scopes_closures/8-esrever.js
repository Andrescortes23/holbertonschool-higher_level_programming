#!/usr/bin/node

exports.esrever = function (list) {
  let a;
  const revers = [];
  for (a = (list.length - 1); a >= 0; a--) {
    revers.push(list[a]);
  }
  return (revers);
};
