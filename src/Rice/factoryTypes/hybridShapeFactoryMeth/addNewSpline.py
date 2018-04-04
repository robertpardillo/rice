
from ...abstractObjects.hybridShapes.spline import Spline


def AddNewSpline(self, geom, objs):
    cat_constructor = self.cat_constructor.AddNewSpline()
    cat_constructor.SetSplineType(0)
    cat_constructor.SetClosing(0)
    part = geom.parentsDict['Part']
    for i in objs:
        cat_constructor.AddPointWithConstraintExplicit(part._createReferenceFromObject(i), None, -1.00000, 1.00000, None, 0.0000)
    geom.cat_constructor.AppendHybridShape(cat_constructor)
    spline = Spline(geom.parentsDict, cat_constructor, objs)
    return spline
