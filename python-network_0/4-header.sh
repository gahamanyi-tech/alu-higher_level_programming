#!/bin/bash
# Sends a GET request to URL with custom header variable
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
