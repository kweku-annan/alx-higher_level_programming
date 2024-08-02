#!/usr/bin/node
const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';
const userTask = {};

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  for (const user of data) {
    const userId = user.userId;
    if (user.completed === true) {
      if (userTask[userId] === undefined) {
        userTask[userId] = 1;
      } else {
        userTask[userId] += 1;
      }
    }
  }
  console.log(userTask);
});
