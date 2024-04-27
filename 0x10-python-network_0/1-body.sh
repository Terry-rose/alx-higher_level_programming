#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sL "$1" -w "%{http_code}" | grep -Fxq "200" && curl -sL "$1" | tail -n +2

