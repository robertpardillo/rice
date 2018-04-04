
from ...abstractObjects.geometric2Delements.controlPoint2D import ControlPoint2D


def AddControlPoint(self, point):
    obj = ControlPoint2D(self.parentsDict._copy(), self, point)
    obj.paint()

    return obj