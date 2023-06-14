#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = Number(process.argv[2]); i > 0; i--) {
    console.log('C is fun');
  }
}
