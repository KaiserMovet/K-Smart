import sys
from ruamel.yaml import YAML

class Types(object):
    def __init__(self):
        self.name = "None"
        self.maxValue = 255
        isRec = "true"
        self.desc = "Some Device Type"
    def to_file(self):
        yaml = YAML()
        yaml.register_class(Types)
        yaml.dump(self, sys.stdout)


temp = Types()
temp.to_file()