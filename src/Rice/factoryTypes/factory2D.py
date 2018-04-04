
from types import MethodType


class Factory2D(object):

    def __init__(self, parent):
        self.parent = parent[parent[-1]]
        self.parentsDict = parent
        self.cat_constructor = self.parent.cat_constructor.Factory2D
        self.imported = dict()

    def __getattr__(self, item):
        item0 = '{}{}'.format(item[0].lower(), item[1:])
        meth = __import__('factoryTypes.2DfactoryMeth.{}'.format(item0), globals(), locals(), [item], level=2)
        meth = meth.__dict__[item]

        self.__setattr__(item, MethodType(meth, self))

        return object.__getattribute__(self, item)

