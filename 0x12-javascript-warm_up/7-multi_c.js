#!/usr/bin/node
const arg = process.argv[2];
const noccur = parseInt(arg);

if (!isNaN(noccur)) {
	for (let i = 0; i < arg; i++) {
		console.log("C is fun");
	}
} else {
	console.log("Missing number of occurrences");
}
