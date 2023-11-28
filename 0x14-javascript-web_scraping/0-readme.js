#!/usr/bin/node

const fs = require('fs');

const readFileAndLogContent = (file) => {
  fs.readFile(file, 'utf-8', (err, data) => {
    if (err) {
      console.error(`Error reading file: ${err.message}`);
    } else {
      console.log(`File contents:\n${data}`);
    }
  });
};

// Check if a file argument is provided
if (process.argv.length < 3) {
  console.error('Usage: node script.js <filename>');
  process.exit(1); // Exit with a non-zero code to indicate an error
}

const file = process.argv[2];
readFileAndLogContent(file);
