#!usr/bin/python3
""" This module writes object to a file using JSON format"""

import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
