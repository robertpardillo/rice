

class Point(object):
    def __init__(self, parent, cat_constructor=None, *args):
        self.parent = parent
        self.cat_constructor = cat_constructor