#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

req.get(url + id, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const characters = data.characters;

  for (const characterUrl of characters) {
    req.get(characterUrl, function (error, res, characterBody) {
      if (error) {
        console.log(error);
      }
      const characterData = JSON.parse(characterBody);
      console.log(characterData.name);
    });
  }
});
