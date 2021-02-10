#!/usr/bin/node

const req = require('request');
let cnt = 0;
const wedge = 'https://swapi-api.hbtn.io/api/people/18/';

req(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const movie = JSON.parse(body).results;
  for (let a = 0; a < movie.length; a++) {
    for (let b = 0; b < movie[a].characters.length; b++) {
      if (movie[a].characters[b] === wedge) {
        cnt += 1;
      }
    }
  }
  console.log(cnt);
});
