
from ..shape import Shape


class CircPattern(Shape):
    """
    Python class to manage Catia's Hybrid Shape Abstract Object. Result of circular patter operation
    """
    def __init__(self, parent, cat_constructor, obj, rotation_axis, instances, deltaTheta):
        """

        :param parent:
        :param cat_constructor:
        :param obj:
        :param rotation_axis:
        :param instances:
        :param deltaTheta:
        """
        super(CircPattern, self).__init__(parent, cat_constructor)
        self.obj = obj
        self. rotationa_axis = rotation_axis
        self.instances = instances
        self.deltaTheta = deltaTheta