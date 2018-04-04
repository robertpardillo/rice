
from ...abstractObjects.hybridShapes.fill import Fill


def AddNewFill(self, geometrical_set, objs):

    cat_constructor = self.cat_constructor.AddNewFill()
    for i in objs:

        try:reference = geometrical_set.parentsDict['Part']._createReferenceFromObject(i._ref_object())
        except:reference = geometrical_set.parentsDict['Part']._createReferenceFromObject(i)
        cat_constructor.AddBound(reference)
    cat_constructor.Continuity = 0
    geometrical_set.cat_constructor.AppendHybridShape(cat_constructor)
    fill = Fill(geometrical_set.parentsDict, cat_constructor, objs)
    return fill