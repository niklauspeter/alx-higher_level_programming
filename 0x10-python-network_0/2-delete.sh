#!/bin/bash
# Sends delete reques to URL passed as argument and displays body of response
curl -sX DELETE "$1"
