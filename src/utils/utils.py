import json

def read_file(file_path: str=None):

    if not file_path:
        file_path = "config.json"

    with open(file_path, "r") as file:
        content = json.load(file)

    return content