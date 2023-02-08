#!/usr/bin/python3

"""function returns object represented by JSON string"""
import json


def from_json_string(my_str):
    """returns object represented by JSON string"""

    return json.load(my_str)
