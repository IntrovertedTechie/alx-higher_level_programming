#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;
  const characterNames = [];

  for (const character of characters) {
    request(character, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      const character = JSON.parse(body);
      characterNames.push(character.name);

      if (characterNames.length === characters.length) {
        for (const name of characterNames) {
          console.log(name);
        }
      }
    });
  }
});
