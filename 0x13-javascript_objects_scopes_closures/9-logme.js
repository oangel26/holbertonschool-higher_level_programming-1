#!/usr/bin/node
let line = 0;

const logMe = (item) => {
  console.log(`${line}: ${item}`);
  line++;
};

exports.logMe = logMe;
