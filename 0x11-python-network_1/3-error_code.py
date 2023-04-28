#!/usr/bin/python3
"""
Script takes in a URL, then sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

from urllib import request, error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    own_request = request.Request(url)
    try:
        with request.urlopen(own_request) as response:
            print(response.read().decode("ascii"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
