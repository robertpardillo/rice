
from ..baseClasses.collection import Collection
from ..generalObjects.sketch import Sketch


class Sketches(Collection):
    def __init__(self, parent):
        super(Sketches, self).__init__(parent, 'Sketches')

    def add(self, *args):
        obj = Sketch(self.parentsDict._copy(), *args)
        self.deque.append(obj)
        return obj

    def item(self, index_name):
        if isinstance(index_name, int):
            return self.deque[index_name]
        elif isinstance(index_name, str):
            for i in self.deque:
                if i.Name == index_name:
                    return i

    def get_boundary(self, name):
        #TODO
        pass


