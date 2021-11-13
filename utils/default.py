import json


def config(filename: str = "./database/config.json"):
    """ Getting a default config file """
    try:
        with open(filename, "r", encoding='utf-8') as data:
            return json.load(data)
    except FileNotFoundError:
        raise FileNotFoundError("JSON file wasn't found")


def saveConfig(load: str, filename: str = "./database/config.json"):
    try:
        with open(filename, "a") as data:
            return json.dump(load, data, indent=2)
    except FileNotFoundError:
        raise FileNotFoundError("JSON file wasn't fount")

