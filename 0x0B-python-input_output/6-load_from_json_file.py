#!/usr/bin/python3
""" This module reads JSON string from a file and converts to python object"""

import json


def load_from_json_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)
