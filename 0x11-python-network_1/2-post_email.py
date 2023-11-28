#!/usr/bin/python3
"""
A python script that accepts a web address (URL) as input
Sends a POST request to the provided URL
Requires an email address as a parameter
Shows the content of the response received from the request
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
