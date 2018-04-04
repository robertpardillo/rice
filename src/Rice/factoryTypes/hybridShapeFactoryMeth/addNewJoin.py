
from ...abstractObjects.hybridShapes.join import Join


def AddNewJoin(self, geometrical_set, objs):
    part = geometrical_set.parentsDict['Part']
    references = list()
    for i in objs:
        references.append(part._createReferenceFromObject(i))
    cat_constructor = self.cat_constructor.AddNewJoin(references[0], references[1])
    for i in range(2, len(references)):
        cat_constructor.AddElement(references[i])

    cat_constructor.SetConnex(1)
    cat_constructor.SetManifold(0)
    cat_constructor.SetSimplify(0)
    cat_constructor.SetSuppressMode(0)
    cat_constructor.SetDeviation(0.001000)
    cat_constructor.SetAngularTolerance(0)
    cat_constructor.SetFederationPropagation(0)
    geometrical_set.cat_constructor.AppendHybridShape(cat_constructor)

    join = Join(geometrical_set.parentsDict, cat_constructor, objs)

    return join