
from ..baseClasses.collection import Collection
from ..generalObjects.relation import Relation
import inspect


class Relations(Collection):
    def __init__(self, parent):
        super(Relations, self).__init__(parent, 'Relations')

    def create_formula(self, name, output, formula, comment):
        if "<class 'Rice.generalObjects.parameter.Parameter'>" in [str(i) for i in inspect.getmro(type(formula))]:
            formula = formula.name

        cat_constructor = self.cat_constructor.CreateFormula(name, comment, output, formula)
        obj = Relation(self.parentsDict._copy(), cat_constructor)
        self.deque.append(obj)
        return obj
