__author__ = 'roberto'


class Factory(object):
    def __init__(self, parent):
        self.imported = {}
        self.parentsDict = parent

    def factory2d(self):
        if 'Factory2D' not in self.imported.keys():
            cls = __import__('factoryTypes.factory2D', globals(), locals(), ['Factory2D'], level=2)
            cls = cls.__dict__['Factory2D']
            self.imported['Factory2D'] = cls(self.parentsDict._copy())

        obj = self.imported['Factory2D']
        return obj

    def shape_factory(self):
        if 'ShapeFactory' not in self.imported.keys():
            cls = __import__('factoryTypes.shapeFactory', globals(), locals(), ['ShapeFactory'], level = 2)
            cls = cls.__dict__['ShapeFactory']
            self.imported['ShapeFactory'] = cls(self.parentsDict._copy())

        obj = self.imported['ShapeFactory']
        return obj

    def hybrid_shape_factory(self):
        """
        Class to contain all hybrid shape operations. If hybrid shape factory has not been created, it is created and then returned.
        If hybrid shape factory has been created it is returned.

        :return:
        """
        if 'HybridShapeFactory' not in self.imported.keys():
            cls = __import__('factoryTypes.hybridShapeFactory', globals(), locals(), ['HybridShapeFactory'], level = 2)
            cls = cls.__dict__['HybridShapeFactory']
            self.imported['HybridShapeFactory'] = cls(self.parentsDict._copy())

        obj = self.imported['HybridShapeFactory']

        return obj
