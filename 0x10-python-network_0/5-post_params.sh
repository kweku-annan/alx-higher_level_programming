#!/bin/bash
# Sends a POST request to a URL
curl -sX POST "email: test@gmail.com; subject: I will always be here for PLD" "$1"
