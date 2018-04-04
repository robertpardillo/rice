
from ..hybridShape import HybridShape


class Spline(HybridShape):
    """
    Spline 3D.
    """
    def __init__(self, parent, cat_constructor, points):
        super(Spline, self).__init__(parent, cat_constructor)
        self.points = points

    def _ref_object(self):
        return self
