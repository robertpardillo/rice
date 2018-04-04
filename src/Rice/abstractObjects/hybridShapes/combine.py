
from ..hybridShape import HybridShape


class Combine(HybridShape):
    """
    Result of combine operation
    """
    def __init__(self, parent, cat_constructor, reference1, reference2, option, plane):
        """

        :param parent: object's parents
        :type: :class:`~Rice.miscellaneous.orderDict.OderDict`
        :param cat_constructor: COM Object
        :type: COM Object
        :param reference1:
        :param reference2:
        :param option:
        :param plane:
        """
        super(HybridShape, self).__init__(parent, cat_constructor)
        self.reference1 = reference1
        self.reference2 = reference2
        self.option = option
        self.plane = plane