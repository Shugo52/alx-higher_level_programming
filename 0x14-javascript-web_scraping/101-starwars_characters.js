#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

request("https://swapi-api.alx-tools.com/api/films/" + id, function (error, reponse, body) {
  if (error) {
    console.log(error);
  } else {
    let results = JSON.parse(body).characters;
    let promises = [];
    for (let i of results) {
      promises.push(new Promise(function (resolve, reject) {
        request(i, (e, r, b) => resolve(JSON.parse(b)['name']));
      }));
    }
    Promise.all(promises).then((a) => {
      for (let i of a) { console.log(i); }
    });
  }
});