
from ...abstractObjects.geometric2Delements.circle2D import Circle2D


def AddArc(self, center, r, start, end):
    obj = Circle2D(self.parentsDict._copy(), self, center, r, start, end)
    obj.paint()
    obj.start_point()
    obj.center_point()
    obj.end_point()

    return obj