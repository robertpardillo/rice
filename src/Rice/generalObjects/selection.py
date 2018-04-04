

class Selection(object):

    def __init__(self, parent):
        """
            parent: document object
        :param parent:
        """
        self.parent = parent[parent[-1]]
        self.parentsDict = parent
        self.cat_constructor = self.parent.cat_constructo.Selection

    def add(self, obj):
        self.cat_constructor.Add()
