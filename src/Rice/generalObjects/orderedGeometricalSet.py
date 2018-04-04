

class OrderedGeometricalSet(object):
    def __init__(self, parent, *args):
        self.parent = parent[parent[-1]]
        self.parentsDict = parent
        self.cat_constructor = self.parent.cat_constructor.Add()
        self.parentsDict[self.name] = self

    @property
    def name(self):
        """
        Get Catia element name
        :return: string
        """
        return self.cat_constructor.Name

    @name.setter
    def name(self, value):
        """
        Set Catia element name
        :param value: string
        :return: None
        """
        self.cat_constructor.Name = value