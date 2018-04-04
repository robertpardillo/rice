
from ..baseClasses.collection import Collection
from ..generalObjects.body import Body


class Bodies(Collection):
    def __init__(self, parent):
        super(Bodies, self).__init__(parent, 'Bodies')

    def add(self, *args):
        """

        Initialize and instance an object of the class imported, then adds it to the deque.

        :param args:
        :return:
        """
        if len(args)>0:
            obj = Body(self.parentsDict._copy(), 'PartBody')
        else:
            obj = Body(self.parentsDict._copy())
        self.deque.append(obj)
        return obj

    def item(self, index_name):
        if isinstance(index_name, int):
            return self.deque[index_name]
        elif isinstance(index_name, str):
            for i in self.deque:
                if i.Name == index_name:
                    return i

