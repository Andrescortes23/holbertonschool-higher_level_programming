#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

req(url, function (error, response, body) {
  if (error) { console.log(error); }
  console.log(JSON.parse(body).title);
});
