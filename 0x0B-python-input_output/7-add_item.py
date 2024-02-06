#!/usr/bin/python3
""""input / output

"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    e_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    e_list = []

if __name__ == "__main__":
    argsa = sys.argv[1:]
    e_list.extend(argsa)
save_to_json_file(e_list, 'add_item.json')
