
from ..baseClasses.collection import Collection
from ..generalObjects.constraint import Constraint

catConstraintTypeDict = {
  "catCstTypeReference":0,
  "catCstTypeDistance":1,
  "catCstTypeOn":2,
  "catCstTypeConcentricity":3,
  "catCstTypeTangency":4,
  "catCstTypeLength":5,
  "catCstTypeAngle":6,
  "catCstTypePlanarAngle":7,
  "catCstTypeParallelism":8,
  "catCstTypeAxisParallelism":9,
  "catCstTypeHorizontality":10,
  "catCstTypePerpendicularity":11,
  "catCstTypeAxisPerpendicularity":12,
  "catCstTypeVerticality":13,
  "catCstTypeRadius":14,
  "catCstTypeSymmetry":15,
  "catCstTypeMidPoint":16,
  "catCstTypeEquidistance":17,
  "catCstTypeMajorRadius":18,
  "catCstTypeMinorRadius":19,
  "catCstTypeSurfContact":20,
  "catCstTypeLinContact":21,
  "catCstTypePoncContact":22,
  "catCstTypeChamfer":23,
  "catCstTypeChamferPerpend":24,
  "catCstTypeAnnulContact":25,
  "catCstTypeCylinderRadius":26,
  "catCstTypeStContinuity":27,
  "catCstTypeStDistance":28,
  "catCstTypeSdContinuity":29,
  "catCstTypeSdShape":30

}


class Constraints(Collection):
    def __init__(self, parent, cat_constructor=None):
        """

        Initialized the object and sketches_COLL to handle the sketches creation.
        Initialized to Factory object.

        :param parent:
        :param cat_constructor:
        :return:
        """
        super(Constraints, self).__init__(parent, 'Constraints')

    def AddBiEltCst(self, CatConstraintType,reference0, reference1):
        constraintType = self._checkConstraint(CatConstraintType)
        reference0_ = self.parentsDict['Part']._createReferenceFromObject(reference0)
        reference1_ = self.parentsDict['Part']._createReferenceFromObject(reference1)
        cat_constructor = self.cat_constructor.AddBiEltCst(catConstraintTypeDict[constraintType], reference0_, reference1_)
        obj = Constraint(self.parentsDict._copy(), cat_constructor, reference0, reference1)
        self.deque.append(obj)
        return obj

    def AddMonoEltCst(self, CatConstraintType,reference0):
        constraintType = self._checkConstraint(CatConstraintType)
        reference0_ = self.parentsDict['Part']._createReferenceFromObject(reference0)
        cat_constructor = self.cat_constructor.AddMonoEltCst(catConstraintTypeDict[constraintType], reference0_)
        obj = Constraint(self.parentsDict._copy(), cat_constructor, reference0)
        self.deque.append(obj)
        return obj

    def AddTriEltCst(self, CatConstraintType, reference0, reference1, reference2):
        constraintType = self._checkConstraint(CatConstraintType)
        reference0_ = self.parentsDict['Part']._createReferenceFromObject(reference0)
        reference1_ = self.parentsDict['Part']._createReferenceFromObject(reference1)
        reference2_ = self.parentsDict['Part']._createReferenceFromObject(reference2)
        cat_constructor = self.cat_constructor.AddTriEltCst(catConstraintTypeDict[constraintType], reference0_,
                                                           reference1_, reference2_)
        obj = Constraint(self.parentsDict._copy(), cat_constructor, reference0, reference1, reference2)
        self.deque.append(obj)
        return obj

    @staticmethod
    def _checkConstraint(CatConstraintType):
        if isinstance(CatConstraintType, int):
            CatConstraintType = [i for i in catConstraintTypeDict if catConstraintTypeDict[i] == CatConstraintType]
        else:
            pass

        return CatConstraintType[0]

    def remove(self, item):
        self.deque.remove(item)
        self.cat_constructor.Remove(item.name)
