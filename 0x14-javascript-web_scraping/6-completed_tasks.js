#!/usr/bin/node
const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';
const userTask = {};

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  for (const user of data) {
    const userId = user.userId;
    userTask[userId] = 0;
  }
  for (const user of data) {
    const userId = user.userId;
    if (user.completed === true) {
      userTask[userId] = userTask[userId] + 1;
    }
  }
  console.log(userTask);
});
