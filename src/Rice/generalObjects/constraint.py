
class Constraint(object):
    def __init__(self, parent, cat_constructor,*args):
        self.parentsDict = parent
        self.parent=parent[parent[-1]]
        self.cat_constructor = cat_constructor
        self.references = [i for i in args]

    @property
    def name(self):
        return self.cat_constructor.Name

    @name.setter
    def name(self, value):
        self.cat_constructor.Name.Value = value

    @property
    def dimension(self):
        return self.cat_constructor.Dimension

    @dimension.setter
    def dimension(self, value):
        self.cat_constructor.Dimension.Value = value

    def remove(self):
        self.parent.remove(self)