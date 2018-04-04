
from ...abstractObjects.geometric2Delements.spline2D import Spline2D


def AddSpline(self, points):
    obj = Spline2D(self.parentsDict._copy(), self, points)
    obj.paint()

    return obj