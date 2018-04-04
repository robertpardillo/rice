
from ..geometry2D import Geometry2D


class ControlPoint2D(Geometry2D):
    def __init__(self, parent, factory2d, point):
        super().__init__(parent)
        self.parent = parent[parent[-1]]
        self.parentsDict = parent
        self.factory2d = factory2d
        self.point = point

    def paint(self):
        self.cat_constructor = self.factory2d.cat_constructor.CreateControlPoint(self.point[0], self.point[1])
        self.parentsDict[self.name] = self
        self.parent._children[self.name] = self
        del self.point


