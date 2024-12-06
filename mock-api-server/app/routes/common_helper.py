"""
Common helper functions
"""
import json


def read_json_file(file_path):
    with open(file_path, 'r') as file_stream:
        data = json.load(file_stream)
    return data
