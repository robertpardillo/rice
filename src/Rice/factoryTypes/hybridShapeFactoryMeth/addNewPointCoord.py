
from ...abstractObjects.hybridShapes.point import PointCoord


def AddNewPointCoord(self, geometric_set, coords=None,reference=None):
    if coords:
        cat_constructor = self.cat_constructor.AddNewPointCoord(coords[0],coords[1],coords[2])
    else:
        cat_constructor = self.cat_constructor.AddNewPointCoord(0.0,0.0,0.0)
    if reference:
        cat_constructor.PtRef = reference
    else:
        pass
    geometric_set.cat_constructor.AppendHybridShape(cat_constructor)
    point = PointCoord(geometric_set.parentsDict, cat_constructor, coords, reference)
    return point