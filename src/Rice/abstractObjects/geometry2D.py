
from .geometricElement import GeometricElement


class Geometry2D(GeometricElement):
    def contruction(self, value):
        """
        Set if the object is a construction element
        :param value:
        :return: bool
        """
        self.cat_constructor.Construction = value

    def __getattribute__(self, item):
        if object.__getattribute__(self, 'isPainted') and item == 'paint':
            return object.__getattribute__(self, '_out')
        elif item == 'paint' and not object.__getattribute__(self, 'isPainted'):
            self.isPainted = True
        return object.__getattribute__(self, item)

    def _out(self):
        print('Already printed')