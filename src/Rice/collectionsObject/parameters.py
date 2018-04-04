
from ..baseClasses.collection import Collection
from ..generalObjects.parameter import Parameter


class Parameters(Collection):
    def __init__(self, parent):
        super(Parameters, self).__init__(parent, 'Parameters')

    def create_real(self, parameterName, value):
        cat_constructor = self.cat_constructor.CreateReal(parameterName, value)
        obj = Parameter(self.parentsDict._copy(),cat_constructor)
        self.deque.append(obj)
        return obj
