
class Shape(object):
    """

    Python class to manage Catia's Shape Abstract Object

    """
    def __init__(self, parent, cat_constructor):
        self.parent = parent[parent[-1]]
        self.parentsDict = parent
        self.cat_constructor = cat_constructor
        self.model_string = "Selection_RSur:(Face:(Brp:({};{};None:();Cf11:());{}_ResultOUT;Z0;G4074)"
        self.parentsDict['Part'].update()

    def _create_reference(self, item):
        if item == 'up':
            reference = self.model_string.format(self.name, "{})".format(2), self.name)
        elif item == 'down':
            reference = self.model_string.format(self.name, "{})".format(1), self.name)
        elif type(item) == int:
            number = self.sketch._children.order('Line.{}'.format(item))
            string2 = "0:(Brp:({};{})))".format(self.sketch.name, number)
            reference = self.model_string.format(self.name, string2, self.name)
        reference = self.parentsDict['Part']._create_reference_from_name(reference)
        return reference

    @property
    def name(self):
        return self.cat_constructor.Name

    @name.setter
    def name(self, value):
        self.cat_constructor.Name = value

    def __getitem__(self, item):
        ref = self._create_reference(item)
        return ref