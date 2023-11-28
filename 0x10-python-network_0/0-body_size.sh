#!/bin/bash
# Bash_Script that takes URL, sends request displays size of body of the response
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
