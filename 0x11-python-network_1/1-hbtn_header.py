#!/usr/bin/python3
"""A script that:recieves in a URL,
- sends  request to the URL and displays the value
- of the X-Request-Id variable found in the header of the response.
"""

import sys
from urllib.request import urlopen
from urllib.parse import urlencode


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('Usage: ', __file__, 'URL', 'email', file=sys.stderr)
        sys.exit(1)

    data = urlencode({'email': sys.argv[2]}).encode()

    with urlopen(sys.argv[1], data=data) as r:
        print(r.read().decode())
