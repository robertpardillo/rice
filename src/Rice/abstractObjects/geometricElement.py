
from Rice.baseClasses.anyObject import AnyObject


class GeometricElement(AnyObject):

    def __init__(self, parent):
        """

        :param parent:
        :param cat_constructor:
        """
        self.isPainted = False
        self.parent = parent[parent[-1]]
        self.parentsDict = parent
        self.parentsDict['Part'].update()


    @property
    def name(self):
        return self.cat_constructor.Name

    @name.setter
    def name(self, value):
        self.cat_constructor.Name = value