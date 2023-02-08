#!/usr/bin/python3

"""function writes an object to text file using json representation."""
import json


def save_to_json_file(my_obj, filename):
    """Write a object to text file using json rep.
    Args:
        filename (str): The name of the file to write.
        my_obj (could be anything): The object to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
