#!/usr/bin/node
const nbOccurences = (list, searchElement) => list.filter(element => element === searchElement).length;
exports.nbOccurences = nbOccurences;
