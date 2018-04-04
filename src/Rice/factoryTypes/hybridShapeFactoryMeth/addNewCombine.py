__author__ = 'roberto'

from ...abstractObjects.hybridShapes.plane import Plane
from ...abstractObjects.hybridShapes.combine import Combine


def AddNewCombine(self, geometric_set, reference1, reference2, option):
    part = geometric_set.parentsDict['Part'].cat_constructor
    reference1 = part.CreateReferenceFromObject(reference1)
    reference2 = part.CreateReferenceFromObject(reference2)
    cat_constructor = self.cat_constructor.AddNewCombine(reference1, reference2, option)
    geometric_set.cat_constructor.AppendHybridShape(cat_constructor)
    plane = Plane(geometric_set.parentsDict, cat_constructor)
    comb = Combine(geometric_set.parentsDict, cat_constructor, reference1, reference2, option, plane)
    return comb