#!/bin/bash
# Sends a GET request to a URL with the required custom header and displays the response body
curl -H "X-School-User-Id: 98" -H "X-HolbertonSchool-User-Id: 98" "$1"
