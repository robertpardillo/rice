__author__ = 'roberto'

from ..baseClasses.collection import Collection
from ..generalObjects.hybridBody import HybridBody


class HybridBodies(Collection):
    """
        Possible Origins:

            Application                         Application                         Application
                Documents                           Documents                           Documents
                    Part                                Part                                Part
                        Bodies                              HybridBodies                        HybridBodies
                            Body                                HybridBody                          HybridBody
                                HybridBodies                                                            HybridBodies
                                    HybridBody                                                              HybridBody



    """
    #TODO
    def __init__(self, parent, *args):
        super(HybridBodies,self).__init__(parent, 'HybridBodies')

    def add(self):
        obj = HybridBody(self.parentsDict._copy())
        super(HybridBodies, self).add(obj)
        return obj

    def item(self, index_name):
        if isinstance(index_name, int):
            return self.deque[index_name]
        elif isinstance(index_name, str):
            for i in self.deque:
                if i.Name == index_name:
                    return i
