
class HybridShape(object):
    """
    Python class to manage Catia's Hybrid Shape Abstract Object
    """
    def __init__(self, parent, cat_constructor):
        """

        :param parent:
        :param cat_constructor:
        """
        self.parent = parent[parent[-1]]
        self.parentsDict = parent
        self.cat_constructor = cat_constructor
        self.parentsDict['Part'].update()

    @property
    def name(self):
        return self.cat_constructor.Name

    @name.setter
    def name(self, value):
        self.cat_constructor.Name = value