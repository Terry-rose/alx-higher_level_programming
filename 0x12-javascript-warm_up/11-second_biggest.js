#!/usr/bin/node

if (process.argv.length <= 2) {
    console.log(0);
} else if (process.argv.length === 3) {
    console.log(0);
} else {
    const numbers = process.argv.slice(2).map(Number).filter((num, index, self) => self.indexOf(num) === index);

    const sortedNumbers = numbers.sort((a, b) => a - b);

    console.log(sortedNumbers[sortedNumbers.length - 2]);
}

