
from ..hybridShape import HybridShape


class Point(HybridShape):
    pass


class PointCoord(Point):
    """
    Point 3D. Point by coord
    """
    def __init__(self, parent, cat_constructor, coords, references):
        super(PointCoord, self).__init__(parent, cat_constructor)
        self.coords = coords
        self.references = references