__author__ = 'roberto'

from ..shape import Shape


class Pocket(Shape):
    """
    Result of pocket operation
    """
    def __init__(self, parent, cat_constructor, sketch, limit):
        super(Pocket, self).__init__(parent, cat_constructor)
        self.sketch = sketch
        self.limit = limit
