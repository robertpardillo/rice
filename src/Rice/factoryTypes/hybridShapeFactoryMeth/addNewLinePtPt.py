
from ...abstractObjects.hybridShapes.line import LinePtPt


def AddNewLinePtPt(self, geometrical_set, start, end):
    part = geometrical_set.parentsDict['Part']
    reference1 = part._createReferenceFromObject(start)
    reference2 = part._createReferenceFromObject(end)
    cat_constructor = self.cat_constructor.AddNewLinePtPt(reference1, reference2)
    geometrical_set.cat_constructor.AppendHybridShape(cat_constructor)
    line = LinePtPt(geometrical_set.parentsDict, cat_constructor, start, end)

    return line