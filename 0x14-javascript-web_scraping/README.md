# 0x14. Javascript - Web scraping

This repository contains assignments for the Holberton School Javascript curriculum.

## Files
- `0-readme.js`: a script that reads and prints the contents of a file in utf-8 encoding. The file path is provided as an argument in the command line.

## Usage
To run the script, make sure you have Node.js installed on your machine. If you haven't installed Node.js, you can download and install it from the official website https://nodejs.org.

1. Clone this repository:


2. Navigate to the `0x14-javascript-web_scraping` directory:


3. Run the script with the file path as an argument:


Replace `<file_path>` with the path of the file you want to read. For example:


This will read the contents of the `cisfun` file (located in the same directory as the script) and print it to the console.

If the file you want to read is located in a different directory, provide the full path to the file in the command. For example:


This will read the contents of the `myfile.txt` file located in the `Documents` directory of the `user` directory and print it to the console.

## Notes
The script reads the file contents asynchronously using the `fs.readFile()` method, so it does not block the event loop. If you need to read large files, consider using a streaming approach to avoid loading the entire file into memory at once.

