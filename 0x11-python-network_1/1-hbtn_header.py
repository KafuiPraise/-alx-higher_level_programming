#!/usr/bin/python3

"""A script that:recieves in a URL,
- sends  request to the URL and displays the value
- of the X-Request-Id variable found in the header of the response.
"""

import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as output:
        req = output.info()
        print(req.get('X-Request-Id'))
