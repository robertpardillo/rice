
from ..geometry2D import Geometry2D


class Point2D(Geometry2D):
    def __init__(self,parent, factory2d,  x, y):
        super().__init__(parent)
        self.parent = parent[parent[-1]]
        self.parentsDict = parent
        self.factory2d = factory2d
        self.values = [x, y]

    def paint(self):
        self.cat_constructor = self.factory2d.cat_constructor.CreatePoint(self.values[0], self.values[1])
        self.parent._children[self.name] = self
        self.parentsDict[self.name] = self

    def __getitem__(self, item):
        return self.values[item]