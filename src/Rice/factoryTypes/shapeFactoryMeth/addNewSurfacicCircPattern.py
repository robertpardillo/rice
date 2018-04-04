
from ...abstractObjects.shapes.circPattern import CircPattern


def AddNewSurfacicCircPattern(self, parent, rotation_axis, instances, deltaTheta, obj):
    part = self.parentsDict['Part'].cat_constructor
    reference1 = part.CreateReferenceFromName("")
    reference2 = part.CreateReferenceFromName("")

    cat_constructor = self.cat_constructor.AddNewSurfacicCircPattern(obj.cat_constructor, 1,2,20.00, 45.00,1,1,reference1,reference2,True,0.0000, True,False)

    cat_constructor.AngularRepartition.AngularSpacing.Value = deltaTheta
    cat_constructor.AngularRepartition.InstancesCount.Value = instances

    reference=part.CreateReferenceFromObject(rotation_axis.cat_constructor)
    cat_constructor.SetRotationAxis(reference)

    circPattern = CircPattern(parent, cat_constructor, obj, rotation_axis, instances, deltaTheta)
    return circPattern

