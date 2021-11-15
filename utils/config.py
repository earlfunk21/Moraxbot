import json
import os


class File:
    def __init__(self):
        self.directory = "database"   # default directory
        if not os.path.isdir(self.directory):
            os.mkdir(self.directory)
        self.filename = "config.json"   # default filename
        self.filepath = os.path.join(self.directory, self.filename)

    def load(self):
        if self.filename not in os.listdir(self.directory):
            load_file = {}
            with open(self.filepath, "w") as f:
                f.write(json.dumps(load_file))
        with open(self.filepath, "r", encoding="utf-8") as data:
            return json.load(data)

    def save(self, load: str):
        with open(self.filepath, "w") as f:
            return json.dump(load, f, indent=2)
