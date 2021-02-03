#!/usr/bin/node
const repeat = parseInt(process.argv[2]);
let ind;
if (isNaN(repeat) === true) {
    console.log("Missing number of occurrences");
} else {
    for (ind = 0; ind < repeat; ind++) {
	console.log("C is fun");
	}
    }
