#!/bin/bash
# POST JSON to URL
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
