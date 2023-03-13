#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];

if (!arg1 || !arg2 || isNaN(arg1) || isNaN(arg2)) {
  console.log('Missing or invalid arguments');
} else {
  const result = add(parseInt(arg1), parseInt(arg2));
  console.log(result);
}
