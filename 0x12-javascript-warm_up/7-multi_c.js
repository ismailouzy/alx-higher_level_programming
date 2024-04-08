#!/usr/bin/node
const arg = process.argv[2];
const noccur = parseInt(arg);

if (!isNaN(noccur) && noccur > 0) {
  for (let i = 0; i < noccur; i++) {
    console.log("C is fun");
  }
} else {
  console.log("Missing number of occurrences");
}
