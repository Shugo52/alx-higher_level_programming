#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let i = 2;
  const array = [];
  while (process.argv[i] !== undefined) {
    array.push(process.argv[i]);
    i++;
  }
  console.log(array.sort(function (a, b) { return (b - a); })[1]);
}
