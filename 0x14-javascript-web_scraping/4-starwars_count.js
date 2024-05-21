#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movies = JSON.parse(body);
    const wedgeMovies = movies.results.filter(movie => {
      return movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/18/`);
    });
    console.log(wedgeMovies.length);
  }
});
