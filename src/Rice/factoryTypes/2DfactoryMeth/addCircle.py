
from ...abstractObjects.geometric2Delements.circle2D import Circle2D


def AddCircle(self, center, r):
    obj = Circle2D(self.parentsDict._copy(), self, center, r, 0, 0)
    obj.paint()
    obj.center_point()

    return obj