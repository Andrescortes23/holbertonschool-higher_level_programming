#!/bin/bash
# Sends a POST request to passed URL, and displays the body of the response
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
