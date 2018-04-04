from ..baseClasses.collection import Collection
from ..generalObjects.factory import Factory


class HybridBody(object):
    """
        Possible Origins:

            Application                         Application                         Application
                Documents                           Documents                           Documents
                    Part                                Part                                Part
                        Bodies                              HybridBodies                        HybridBodies
                            Body                                HybridBody                          HybridBody
                                HybridBodies                                                            HybridBodies
                                    HybridBody                                                              HybridBody

        HybridBody object

        Object variables:


    """
    #TODO
    def __init__(self, parent, *args):
        self.parent = parent[parent[-1]]
        self.parentsDict = parent
        self.cat_constructor = self.parent.cat_constructor.Add()
        self.parentsDict[self.name] = self
        self.factory = Factory(self.parentsDict)

    @property
    def name(self):
        """
        Get Catia element name
        :return: string
        """
        return self.cat_constructor.Name

    @name.setter
    def name(self, value):
        """
        Set Catia element name
        :param value: string
        :return: None
        """
        self.cat_constructor.Name = value

    def add_sketch(self, plane):
        """
        Add sketch to geometrical set
        :param plane:
        :return:
        """
        try:
            if plane.lower() in ['xy', 'yx', 'zx', 'xz', 'zy', 'yz']:
                plane = self.parent.parent.originElements.get(plane)
        except:
            pass
        try :
            self.__getattribute__('sketches_COLL')
        except AttributeError:
            self.sketches_COLL = Collection(self.parentsDict._copy(), 'collectionsObject.sketchesF.sketches.Sketch', 'HybridSketches')

        self.sketches_COLL.add(plane)

        return self.sketches_COLL.deque[-1]

    def plane(self, option, reference, *args):
        """
        Add plane
        :param option: string,
        :param reference:
        :param args:
        :return:
        """
        if reference.lower() in ['xy','yx','zx','xz','zy','yz']:
            reference = self.parent.parent.originElements.get(reference).cat_constructor
        hybridFactory = self.factory.hybrid_shape_factory()
        if option == 'Offset from plane':

            try: reverse = args[1]
            except:reverse = False
            plane = hybridFactory.AddNewPlaneOffset(self, reference, args[0], reverse)
        elif option == 'Angle/Normal to plane':
            pass
        else:
            pass
        return plane

    def combine(self, sketch1, sketch2, option=0):
        """
        Combine operation
        :param sketch1:
        :param sketch2:
        :param option:
        :return:
        """
        hybridFactory = self.factory.hybrid_shape_factory()
        comb = hybridFactory.AddNewCombine(self, sketch1, sketch2, option)
        return comb
