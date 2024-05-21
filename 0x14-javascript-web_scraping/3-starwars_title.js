#!/usr/bin/node
// A script that prints the title of a Star Wars movie where the episode num matches a given int

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
