#!/bin/bash
# Script sends request to particular URL and
# Get the byte size of the HTTP response header.
curl -s "$1" | wc -c
