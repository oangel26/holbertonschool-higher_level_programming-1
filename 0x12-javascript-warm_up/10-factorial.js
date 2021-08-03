#!/usr/bin/node
const argv = process.argv;

const number = parseInt(argv[2]);

const factorial = number => {
  if (number === 0) {
    return (1);
  }
  return (number * factorial(number - 1));
};

if (isNaN(number)) {
  console.log(1);
} else {
  console.log(factorial(number));
}
