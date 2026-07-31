#!/bin/bash
# Sends a GET request to a URL with the X-School-User-Id header and displays the response body
curl -H "X-School-User-Id: 98" "$1"
