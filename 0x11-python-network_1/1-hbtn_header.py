import sys
import urllib.request

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a URL.")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.headers.get("X-Request-Id")
            print(f"X-Request-Id: {x_request_id}")
    except urllib.error.URLError as e:
        print(f"Error: {e}")
