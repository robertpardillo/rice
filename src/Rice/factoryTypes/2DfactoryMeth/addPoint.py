
from ...abstractObjects.geometric2Delements.point2D import Point2D


def AddPoint(self, xc, yc):
    obj = Point2D(self.parentsDict._copy(), self, xc, yc)
    obj.paint()

    return obj