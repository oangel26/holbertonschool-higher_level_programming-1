#!/usr/bin/node
const esrever = (list) => {
  const result = [];

  for (let i = list.length - 1; i >= 0; i--) {
    result.push(list[i]);
  }
  return result;
};

exports.esrever = esrever;
