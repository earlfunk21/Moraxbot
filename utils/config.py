import json
import os




def load(filename: str = "config.json"):
    with open(filename, "r", encoding="utf-8") as data:
        return json.load(data)

