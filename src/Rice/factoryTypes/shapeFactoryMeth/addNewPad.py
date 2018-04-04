
from ...abstractObjects.shapes.pad import Pad


def AddNewPad(self, parent,  sketch, limit):
    cat_constructor = self.cat_constructor.AddNewPad(sketch.cat_constructor, limit)
    pad = Pad(parent, cat_constructor, sketch, limit)
    return pad