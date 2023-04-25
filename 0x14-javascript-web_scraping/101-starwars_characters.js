#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const characters = JSON.parse(body).characters;

  printCharacters(characters, 0);
});

function printCharacters(characters, idx) {
  if (idx >= characters.length) return;

  request(characters[idx], function (error, response, body) {
    if (error) {
      console.error(error);
      return;
    }
    console.log(JSON.parse(body).name);
    printCharacters(characters, idx + 1);
  });
}
