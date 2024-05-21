#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);
    const completedTasksByUser = {};

    tasks.forEach(task => {
      if (task.completed) {
        const userId = task.userId.toString();
        if (!completedTasksByUser[userId]) {
          completedTasksByUser[userId] = 1;
        } else {
          completedTasksByUser[userId]++;
        }
      }
    });

    console.log(completedTasksByUser);
  }
});
