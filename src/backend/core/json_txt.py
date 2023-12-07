import os
import json


def write_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f)

    return data


def read_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
    else:
        data = []
        write_json(data)

    return data


def read_txt(file_path):
    with open(file_path, "r") as f:
        data = f.read().split("\n")

    return data
