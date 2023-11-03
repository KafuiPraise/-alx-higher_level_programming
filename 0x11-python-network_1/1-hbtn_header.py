#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header of the response.
"""

import sys
import urllib.request

if __name__ == "__main__":
    # Check if the user provided a URL as a command-line argument
    if len(sys.argv) < 2:
        print("Please provide a URL.")
        sys.exit(1)

    # Get the URL from the command-line arguments
    url = sys.argv[1]

    # Send a request to the specified URL
    try:
        with urllib.request.urlopen(url) as response:
            # Retrieve and print the value of the "X-Request-Id" header
            x_request_id = response.headers.get("X-Request-Id")
            print(f"X-Request-Id: {x_request_id}")
    except urllib.error.URLError as e:
        print(f"Error: {e}")

