import re


class Parameter(object):
    def __init__(self, parent, cat_constructor):
        self.parent = parent[parent[-1]]
        self.parentsDict = parent
        self.cat_constructor = cat_constructor

    @property
    def name(self):
        name = self.cat_constructor.Name
        name_s = re.findall(".*\\\(.*)", name)[0]
        return name_s

    @name.setter
    def name(self, value):
        self.cat_constructor.Name = value

