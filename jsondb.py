import os, json
from pathlib import Path

objects = {}
def Object(file) :
    if not file in objects:
        objects[file] = _Object(file)
    return objects[file]

class _Object:
    def __init__(self, file):
        self.dirty = False
        self.file = file
        self.data = {}
        if os.path.exists(self.file):
            with open(self.file, "r") as f :
                self.data = json.load(f)

    def __getitem__(self,key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.dirty = True
        self.data[key] = value

    def __contains__(self, key):
        return key in self.data

    def path(self) :
        return Path(self.file)

    def save(self, force=False):
        if not self.dirty and not force:
            pass
        with open(self.file, "w") as f:
            json.dump(self.data, f)
        self.dirty = False

