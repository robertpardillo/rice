__author__ = 'roberto'

from ...abstractObjects.geometry2D import Geometry2D


class Spline2D(Geometry2D):
    def __init__(self, parent, factory2d, points):
        super().__init__(parent)
        self.parent = parent[parent[-1]]
        self.parentsDict = parent
        self.factory2d = factory2d
        self.points = points

    def _ref_object(self):
        return self.parentsDict[self.parentsDict[-2]]

    def paint(self):
        list_of_control = list()
        self.control_points=list()
        for i in self.points:
            control_point = self.factory2d.AddControlPoint(i)
            self.control_points.append(control_point)
            list_of_control.append(control_point.cat_constructor)
        self.cat_constructor = self.factory2d.cat_constructor.CreateSpline(list_of_control)
        self.parentsDict[self.name] = self
        self.parent._children[self.name] = self

