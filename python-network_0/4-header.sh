#!/bin/bash
# Sends a GET request to a URL with the X-HolbertonSchool-User-Id header and displays the response body
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
