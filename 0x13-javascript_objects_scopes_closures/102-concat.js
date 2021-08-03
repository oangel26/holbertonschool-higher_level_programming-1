#!/usr/bin/node

const fs = require('fs');

const getPaths = () => {
  let { argv } = process;
  argv = argv.slice(2);
  return {
    file1: argv[0],
    file2: argv[1],
    dest: argv[2]
  };
};

const checkPaths = (paths) => {
  return !!paths.file1 || !!paths.file2 || !!paths.dest;
};

const readFile = (path) => fs.readFileSync(path, 'utf8');

const paths = getPaths();
if (checkPaths(paths)) {
  const data1 = readFile(paths.file1);
  const data2 = readFile(paths.file2);
  const content = data1.concat(data2);
  fs.writeFileSync(paths.dest, content);
}
