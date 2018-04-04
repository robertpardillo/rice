
from ..baseClasses.collection import Collection


class GeometricElements(Collection):

    def __init__(self, parent):
        super(GeometricElements, self).__init__(parent, 'GeometricElements')

    def add(self, obj):
        super(GeometricElements, self).add(obj)
