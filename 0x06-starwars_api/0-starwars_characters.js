#!/usr/bin/node

const request = require('request');
const URL = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
// https://swapi-api.alx-tools.com/

request(URL, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const newObject = JSON.parse(body);
    const characters = newObject.characters;
    // Promises return value holder
    const castNames = [];
    // getting each character name from each given endpoint
    for (let i = 0; i < characters.length; i++) {
      // appending Promises to the list
      castNames.push(
        new Promise((resolve, reject) => {
          // getting the correct URL
          const namesEndPoint = characters[i];
          // retriving data from the given endpoint
          request(namesEndPoint, (error, response, body) => {
            if (!error && response.statusCode === 200) {
              // getting data from raw json
              const resp = JSON.parse(body);
              // actual characterName
              resolve(resp.name);
            } else {
              // somethings wrong with the URL
              reject(error);
            }
          });
        }),
      );
    }
    // Taking all the iterable(Promises) and recording in the executing them in the same order
    Promise.all(castNames).then((castNamesList) => {
      // getting the promises resolve value and printing them in the same order
      castNamesList.forEach((charName) => console.log(charName));
    });
  }
});
