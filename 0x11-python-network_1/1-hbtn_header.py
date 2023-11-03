#!/usr/bin/python3
"""
A python script that takes in a URL,
sends a request and displays the value 
of the X-Request-Id variable found in the header of the response.
"""

import sys
import urllib.request

if __name__ == "__main__":
    # Check if the user provided a URL as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
        sys.exit(1)

    # Get the URL from the command-line argument
    url = sys.argv[1]

    try:
        # Send a GET request to the specified URL
        with urllib.request.urlopen(url) as response:
            # Extract and print the value of the "X-Request-Id" header from the response
            request_id = response.headers.get("X-Request-Id")
            if request_id:
                print(f"X-Request-Id: {request_id}")
            else:
                print("X-Request-Id header not found in the response.")
    except urllib.error.HTTPError as e:
        print(f"Error: {e}")
    except urllib.error.URLError as e:
        print(f"Error: {e}")
