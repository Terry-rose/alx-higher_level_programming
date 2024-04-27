#!/usr/bin/node

function factorial(n) {
    if (n === 0 || n === 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

if (process.argv[2] === undefined || isNaN(parseInt(process.argv[2]))) {
    console.log(1);
} else {
    const result = factorial(parseInt(process.argv[2]));
    console.log(result);
}

