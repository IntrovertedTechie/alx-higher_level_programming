#!/bin/bash
# This script takes in a URL, sends a request to that URL using curl,
# and displays the size of the body of the response in bytes.

url="$1"
response=$(curl -sI "$url" | grep -i 'Content-Length' | awk '{print $2}')
echo "$response"

