
from ...abstractObjects.geometric2Delements.point2D import Point2D
from ...abstractObjects.geometric2Delements.line2D import Line2D


def AddLine(self, start, end):
    obj = Line2D(self.parentsDict._copy(), self, start, end)
    obj.paint()

    return obj