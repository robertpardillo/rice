
from ..hybridShape import HybridShape


class Fill(HybridShape):
    """
    Result of fill operation.
    """
    def __init__(self, parent, cat_constructor, references):
        super(Fill, self).__init__(parent, cat_constructor)
        self.objs = references