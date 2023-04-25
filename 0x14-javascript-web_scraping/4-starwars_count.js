#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const results = JSON.parse(body).results;
  let count = 0;
  for (const movie of results) {
    for (const character of movie.characters) {
      if (character.endsWith('/18/')) {
        count++;
        break;
      }
    }
  }
  console.log(count);
});
