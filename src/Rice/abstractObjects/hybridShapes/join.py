
from ..hybridShape import HybridShape


class Join(HybridShape):
    """
    Result of join operation
    """
    def __init__(self, parent, cat_constructor, objs):
        super(Join, self).__init__(parent, cat_constructor)
        self.objs = objs