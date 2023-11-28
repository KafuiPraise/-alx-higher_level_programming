#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = countCharactersInFilms(films, '18');
    console.log(count);
  } else {
    console.log('An error occurred. Status code: ' + response.statusCode);
  }
});

function countCharactersInFilms(films, targetCharacterId) {
  let count = 0;
  for (const filmIndex in films) {
    const filmChars = films[filmIndex].characters;
    for (const charIndex in filmChars) {
      if (filmChars[charIndex].includes(targetCharacterId)) {
        count++;
      }
    }
  }
  return count;
}
