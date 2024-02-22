#!/usr/bin/python3
"""This script adds all arguments to a Python List, and then save them to
a file"""
import json
import sys
save_to = __import__('5-save_to_json_file').save_to_json_file
load_from = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
args_list = []
try:
    args_list = load_from(filename)
except FileNotFoundError:
    args_list = []

if len(sys.argv) >= 2:
    for i in sys.argv[1:]:
        args_list.append(i)

save_to(args_list, filename)
