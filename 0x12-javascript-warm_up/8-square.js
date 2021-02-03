#!/usr/bin/node

const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let ind = 0; ind < size; ind++) {
    console.log('X'.repeat(size));
  }
}
