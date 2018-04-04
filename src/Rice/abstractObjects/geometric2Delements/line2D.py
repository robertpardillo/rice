
from ...abstractObjects.geometric2Delements.point2D import Point2D
from ...miscellaneous.stdOutput import output
from ..geometry2D import Geometry2D


class Line2D(Geometry2D):
    def __init__(self,parent, factory2d, start, end):
        super(Line2D, self).__init__(parent)
        self.parent = parent[parent[-1]]
        self.parentsDict = parent
        self.factory2d = factory2d
        self.start = start
        self.end = end

    def paint(self):
        x1 = self.start[0]
        y1 = self.start[1]

        x2 = self.end[0]
        y2 = self.end[1]

        if isinstance(self.start, Point2D):
            pass
        else:
            output('changing values of line from list to Point2D objects')

            self.start = self.factory2d.AddPoint(x1, y1)

        if isinstance(self.end, Point2D):
            pass
        else:
            output('changing values of line from list to Point2D objects')

            self.end = self.factory2d.AddPoint(x2, y2)

        self.cat_constructor = self.factory2d.cat_constructor.CreateLine(x1, y1, x2, y2)
        self.parentsDict[self.name] = self
        self.parent._children[self.name] = self

    def start_point(self):
        self.start.paint()
        self.cat_constructor.StartPoint = self.start.cat_constructor

    def end_point(self):
        self.end.paint()
        self.cat_constructor.EndPoint = self.end.cat_constructor
