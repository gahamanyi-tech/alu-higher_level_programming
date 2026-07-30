#!/bin/bash
# Sends a GET request with custom header X-HolbertonSchool-User-Id: 98
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
