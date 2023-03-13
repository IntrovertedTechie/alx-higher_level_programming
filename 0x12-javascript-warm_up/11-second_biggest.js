#!/usr/bin/node

function secondBiggestInt (args) {
  // Convert all arguments to integers
  const nums = args.map(Number);

  // Sort the array in descending order
  nums.sort((a, b) => b - a);

  // Return the second biggest integer or 0 if it doesn't exist
  return nums[1] || 0;
}

const args = process.argv.slice(2); // Ignore the first two arguments
const result = secondBiggestInt(args);

console.log(result);
