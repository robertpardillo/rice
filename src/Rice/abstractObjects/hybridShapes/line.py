
from ..hybridShape import HybridShape
from ...baseClasses.anyObject import AnyObject


class Line(HybridShape):
    pass


class LinePtPt(Line):
    """
    Result of operation line 3D. Option point to point
    """
    def __init__(self, parent, cat_constructor, start, end):
        super(LinePtPt, self).__init__(parent, cat_constructor)
        self.start = start
        self.end = end
