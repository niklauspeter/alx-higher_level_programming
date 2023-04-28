#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response."""

from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = request.Request(url)
    with request.urlopen(req) as response:
        print(dict(response.headers).get('X-request-Id'))
