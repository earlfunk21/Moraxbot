import json
import os


class File:
    def __init__(self, directory: str = "database", filename: str = "config.json"):
        self.directory = directory
        self.filename = filename

    def _checkFile(self):
        if not os.path.isdir(self.directory):
            os.mkdir(self.directory)
            if not os.path.isdir(self.directory):
                raise f"{self.directory} not found!"
        if self.filename not in os.listdir(self.directory):
            load_file = {}
            with open(os.path.join(self.directory, self.filename), "w") as f:
                f.write(json.dumps(load_file))

    def load(self):
        self._checkFile()
        with open(os.path.join(self.directory, self.filename), "r", encoding="utf-8") as data:
            return json.load(data)

    def save(self, load: str, opt: str = "w"):
        self._checkFile()
        with open(os.path.join(self.directory, self.filename), opt) as f:
            return json.dump(load, f, indent=2)
