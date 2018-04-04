
from ..abstractObjects.hybridShapes.plane import Plane


class OriginElements(object):
    def __init__(self, parent):
        self.parent = parent[parent[-1]]
        self.parentsDict = parent
        self.cat_constructor = self.parent.cat_constructor.OriginElements
        self.parentsDict['OriginElements'] = self
        self.originsPlanes = dict()

        self.originsPlanes['xy'] = Plane(self.parentsDict, self.cat_constructor.PlaneXY)
        self.originsPlanes['yz'] = Plane(self.parentsDict, self.cat_constructor.PlaneYZ)
        self.originsPlanes['zx'] = Plane(self.parentsDict, self.cat_constructor.PlaneZX)

    def get(self, plane):
        if plane.lower() in ['xy', 'yx']:
            plane = 'xy'
        elif plane.lower() in ['yz', 'zy']:
            plane = 'yz'
        elif plane.lower() in ['zx', 'xz']:
            plane = 'zx'
        return self.originsPlanes[plane]

    @property
    def name(self):
        return self.cat_constructor.Name

    @name.setter
    def name(self, value):
        self.cat_constructor.Name = value
