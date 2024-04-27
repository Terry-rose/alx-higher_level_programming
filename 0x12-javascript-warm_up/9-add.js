#!/usr/bin/node

function add(a, b) {
    return a + b;
}

if (process.argv[2] === undefined || process.argv[3] === undefined) {
    console.log("NaN");
} else {
    const result = add(parseInt(process.argv[2]), parseInt(process.argv[3]));
    console.log(result);
}

