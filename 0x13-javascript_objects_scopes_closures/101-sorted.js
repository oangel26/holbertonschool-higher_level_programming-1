#!/usr/bin/node

const { dict } = require('./101-data');

const result = {};
Object.entries(dict).forEach(([key, value]) => {
  result[value] = result[value] ? result[value] : [];
  result[value].push(key);
});
console.log(result);
