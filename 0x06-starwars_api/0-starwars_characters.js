#!/usr/bin/node

const request = require('request');
const process = require('process');

const handleRequest = async (url) => {
  return new Promise((resolve, reject) => {
    request(url, function (error, response, body) {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

const getCharacterData = async (url) => {
  const characterData = await handleRequest(url);
  return characterData.name;
};

const getMovieData = async (number) => {
  const movieData = await handleRequest('https://swapi-api.alx-tools.com/api/films/' + number + '/');
  const characters = movieData.characters;
  for (const entry in characters) {
    const characterData = await getCharacterData(characters[entry]);
    console.log(characterData);
  }
};

getMovieData(process.argv[2]);
