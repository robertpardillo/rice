
from ..baseClasses.collection import Collection
from ..generalObjects.orderedGeometricalSet import OrderedGeometricalSet


class OrderedGeometricalSets(Collection):
    """
    Ordered geometrical set object
    """
    def __init__(self, parent, *args):
        """

        :param parent:
        :rtype: :class:´~Rice.miscellaneous.orderDict.OrderDict´
        :param args:
        """
        super(OrderedGeometricalSets, self).__init__(parent, 'OrderedGeometricalSets')

    def add(self):
        obj = OrderedGeometricalSet(self.parentsDict._copy())
        super(OrderedGeometricalSets, self).add(obj)
        return obj

    @property
    def name(self):
        return self.cat_constructor.Name

    @name.setter
    def name(self, value):
        self.cat_constructor.Name = value