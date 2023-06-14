#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  let i = parseInt(process.argv[2]);
  const x = i;
  for (i; i > 0; i--) {
    console.log('X'.repeat(x));
  }
}
