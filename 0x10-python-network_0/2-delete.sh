#!/bin/bash
# Sends DELETE request to URL passed as argument and displays body of response.
curl -sX DELETE "$1"
