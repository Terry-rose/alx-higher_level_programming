#!/usr/bin/node

if (process.argv[2] === undefined || isNaN(parseInt(process.argv[2]))) {
    console.log("Missing number of occurrences");
} else {
    const x = parseInt(process.argv[2]);

    for (let i = 0; i < x; i++) {
        console.log("C is fun");
    }
}

