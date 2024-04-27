#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument, using the contents of a file passed as the second argument, and displays the body of the response

# Check if the number of arguments is valid
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 URL JSON_FILE"
    exit 1
fi

# Check if the JSON file exists
if [ ! -f "$2" ]; then
    echo "Error: JSON file '$2' not found"
    exit 1
fi

# Send the POST request with the JSON file content in the body and display the response body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"

