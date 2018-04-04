__author__ = 'roberto'

from ...abstractObjects.shapes.pocket import Pocket


def AddNewPocket(self, parent, sketch, limit):
    construc = self.cat_constructor.AddNewPocket(sketch.cat_constructor, limit)
    poc = Pocket(parent, construc, sketch, limit)
    return poc