#!/usr/bin/python3
"""This module converts JSON string to its respective python object"""
import json


def from_json_string(my_str):
    return json.loads(my_str)
