#!/bin/bash
# Displays status code of a request
curl -sw "%{http_code}" "$1"
