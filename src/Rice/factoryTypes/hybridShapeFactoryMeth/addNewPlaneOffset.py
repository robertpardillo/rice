
from ...abstractObjects.hybridShapes.plane import PlaneOffset


def AddNewPlaneOffset(self, geometrical_set, reference, offset, reverse_direction=False):
    reference_1 = self.parentsDict['Part']._createReferenceFromObject(reference)
    cat_constructor = self.cat_constructor.AddNewPlaneOffset(reference_1, offset, reverse_direction)
    geometrical_set.cat_constructor.AppendHybridShape(cat_constructor)
    cat_constructor = geometrical_set.cat_constructor.HybridShapes.Item(cat_constructor.Name)
    geometrical_set.parentsDict['Part'].update()
    plane = PlaneOffset(self.parentsDict, cat_constructor, reference)
    return plane

