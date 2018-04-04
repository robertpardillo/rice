
from ..hybridShape import HybridShape


class Plane(HybridShape):
    pass


class PlaneOffset(Plane):
    def __init__(self, parentsDict, cat_constructor, reference):
        """

        :param parentsDict: Parents
        :type parentsDict: :class:`~Rice.miscellaneous.orderDict.OrderDict`
        :param cat_constructor: COM Object
        :type cat_constructor: COM Object
        :param reference: reference plane
        :type reference: :class:`~Rice.abstractObjects.hybridShapes.plane.Plane`
        """
        super(PlaneOffset, self).__init__(parentsDict, cat_constructor)
        self.reference = reference

    def offset(self):
        return self.cat_constructor.Offset