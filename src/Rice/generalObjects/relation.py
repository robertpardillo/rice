
class Relation(object):
    def __init__(self, parent, cat_constructor):
        self.parent = parent[parent[-1]]
        self.parentsDict = parent
        self.cat_constructor = cat_constructor
