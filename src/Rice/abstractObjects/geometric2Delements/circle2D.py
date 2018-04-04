
import numpy as np
from .point2D import Point2D
from ..geometry2D import Geometry2D


class Circle2D(Geometry2D):
    def __init__(self, parent, factory2d, center, r, start, end):
        super().__init__(parent)
        self.parent = parent[parent[-1]]
        self.parentsDict = parent
        self.factory2d = factory2d
        self.values = [center, r, start, end]

    def paint(self):
        self.cat_constructor = self.factory2d.cat_constructor.CreateCircle(self.values[0][0],self.values[0][1],self.values[1],
                                                                self.values[2],self.values[3])

        self.parent._children[self.name] = self
        self.parentsDict[self.name] = self

    def center_point(self):
        if isinstance(self.values[0], Point2D):
            pass
        else:
            point = self.factory2d.AddPoint(self.values[0][0], self.values[0][1])
            point.paint()
            self.values[0] = point
        self.cat_constructor.CenterPoint = self.values[0].cat_constructor

    def start_point(self):
        xs = self.values[0][0] + self.values[1]*np.cos(self.values[2])
        ys = self.values[0][1] + self.values[1]*np.sin(self.values[2])

        p_start = self.factory2d.AddPoint(xs, ys)
        p_start.paint()
        self.values[2] = p_start

        self.cat_constructor.StartPoint = p_start.cat_constructor

    def end_point(self):
        xe = self.values[0][0] + self.values[1]*np.cos(self.values[3])
        ye = self.values[0][1] + self.values[1]*np.sin(self.values[3])

        p_end = self.factory2d.AddPoint(xe, ye)
        p_end.paint()
        self.values[3] = p_end

        self.cat_constructor.EndPoint = p_end.cat_constructor

    def changePoint(self,point, newx,newy):
        if point=='start':
            point = self.factory2d.AddPoint(newx,newy)
            point.paint()
            self.values[2]= point
            self.cat_constructor.StartPoint = point

        elif point=='end':
            point = self.factory2d.AddPoint(newx,newy)
            point.paint()
            self.values[3]= point
            self.cat_constructor.EndPoint = point
