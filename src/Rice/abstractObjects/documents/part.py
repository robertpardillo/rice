

from ...generalObjects.factory import Factory
from ...generalObjects.originElements import OriginElements
from ...collectionsObject.hybridBodies import HybridBodies
from ...collectionsObject.bodies import Bodies
from ...collectionsObject.parameters import Parameters
from ...collectionsObject.relations import Relations
from ...collectionsObject.orderedGeometricalSets import OrderedGeometricalSets
from ...baseClasses.anyObject import AnyObject


class Part(AnyObject):
    """
    Catia's PART object
    """
    def __init__(self, parent=None):

        self.parent = parent[parent[-1]]
        self.parentsDict = parent
        self.cat_constructor = self.parent.cat_constructor.Part
        self.parentsDict[self.name] = self
        self.bodies_COLL = Bodies(self.parentsDict._copy())
        self.bodies_COLL.add('PartBody')

        self.originElements = OriginElements(self.parentsDict._copy())

        self.factory = Factory(self.parentsDict)

    @property
    def name(self):
        """
        Return the Catia's element name

        :return:
        :rtype: str
        """
        return self.cat_constructor.Name

    @name.setter
    def name(self, value):
        """
        Set the Catia's element name
        """
        self.cat_constructor.Name = value

    def add_body(self):
        """
        Add a body to the part

        :return:  Last Body created
        :rtype: :class:`~Rice.generalObjects.body.Body`
        """
        self.bodies_COLL.add()
        return self.bodies_COLL.deque[-1]

    def get_geometrical_set(self):
        """
        Get all geometrical sets

        :return: list of geometrical sets created
        :rtype: list of :class:`~Rice.generalObjects.hybridBody.HybridBody`
        """
        return self.hybrid_bodies_COLL.deque

    def get_bodies(self):
        """
        Get all created bodies.

        :return: list of created bodies
        :rtype: list of :class:`~Rice.generalObjects.body.Body`
        """
        return self.bodies_COLL.deque

    def _create_reference_from_name(self, reference):
        obj = self.cat_constructor.CreateReferenceFromName(reference)
        return obj

    def add_ordered_geometrical_set(self):
        """
        Add an ordered geometrical set

        :return: Last OrderedGeometricalSet
        :rtype: :class:`~Rice.generalObjects.orderedGeometricalSet.OrderedGeometricalSet`
        """
        try:
            self.ordered_geometrical_set_COLL.add()

        except AttributeError:
            self.ordered_geometrical_set_COLL = OrderedGeometricalSets(self.parentsDict._copy())
            self.ordered_geometrical_set_COLL.add()
        return self.ordered_geometrical_set_COLL.deque[-1]

    def get_ordered_geometrical_set(self):
        """
        Get all ordered geometrical sets created
        :return:
        :rtype: list of :class:`~Rice.generalObjects.orderedGeometricalSet.OrderedGeometricalSet`
        """
        return self.ordered_geometrical_set_COLL.deque

    def geometrical_set(self):
        """
        Add a geometrical set or get the geometrical sets created

        :return: Last geometricalSet or list of geometricalSet
        :rtype: list of :class:`~Rice.generalObjects.hybridBody.HybridBody` or :class:`~Rice.generalObjects.hybridBody.HybridBody`
        """
        try:
            return self.hybrid_bodies_COLL

        except AttributeError:
            self.hybrid_bodies_COLL = HybridBodies(self.parentsDict._copy())
            self.hybrid_bodies_COLL.add()
            return self.hybrid_bodies_COLL.deque[-1]
    """
    def setting(self):
        
        Add a settings object to change Catia's settings

        :return: Last or list of settings object (:py:class:`~collectionsObject.settingsF.settings.Settings`)
        
        try:
            return self.setting_COLL

        except AttributeError:
            self.setting_COLL = Collection(self.parentsDict['CNEXT'].parentsDict._copy(), 'collectionsObject.settingF.setting.Settings', 'SettingControllers')
            self.setting_COLL.add()
            return self.setting_COLL.deque[-1]
    """
    def plane(self, option, reference, *args):
        """
        Create a plane on Part.

            +---------------------------+-------------------------------------------------------+
            |        option             |      args                                             |
            +---------------------------+-------------------------------------------------------+
            |    Offset from plane      |   (distance, reverse )                                |
            |                           |                                                       |
            |                           |    distance: <float>                                  |
            |                           |        Distance from reference to new plane           |
            |                           |    reverse: <boolean>                                 |
            |                           |        True ---> reverse direction                    |
            |                           |        False --> not reverse                          |
            +---------------------------+-------------------------------------------------------+
            |                                                                                   |
            |     Only implemented for offset from plane                                                                          |
            +---------------------------+-------------------------------------------------------+

        :param option: options, see docstring to more information
        :type option: str
        :param reference:
        :type reference: str or :class:`~Rice.abstractObjects.hybridShapes.plane.Plane`
        :param args: list of arguments needed
        :return: Created plane
        :rtype: :class:`~Rice.abstractObjects.hybridShapes.plane.Plane`
        """
        self.geometrical_set()
        if reference.lower() in ['xy','yx','zx','xz','zy','yz']:
            reference = self.originElements.get(reference)
        hybridFactory = self.factory.hybrid_shape_factory()
        if option == 'Offset from plane':
            try: reverse = args[1]
            except:reverse = False
            plane = hybridFactory.AddNewPlaneOffset(self.hybrid_bodies_COLL.deque[-1], reference, args[0], reverse)
        elif option == 'Angle/Normal to plane':
            pass
        else:
            pass
        return plane

    def export_data(self, file_path, extension):
        """
        Exports CATPart to other format.

        Extension:
            - stl
            - igs
            - model
            - stp
            - 3dmap
            - 3dxml
            - cgr
            - hcg
            - icem
            - NavRep
            - vps
            - wrl

        :param file_path
        :type file_path: str
        :param extension: type of exported data
        :type extension: str
        """
        self.parent.export_data(file_path, extension)

    def save(self, file_path):
        """
        Path to saved file
        :param file_path: path
        :type file_path: str
        """
        self.parent.save(file_path)

    def line3D(self, start, end, st1=None,sl1=None,st2=None, sl2=None,geometrical_set=None): #OJOOOOOOOOOOOOOOOOOOoo cambiado
        """

        Create a 3D line from two points.

        :param start: Start Point
        :type start: list of float or :class:`~Rice.abstractObjects.hybridShapes.point.PointCoord`
        :param end: End point
        :type end: list of float or :class:`~Rice.abstractObjects.hybridShapes.point.PointCoord`
        :param st1: TODO
        :param sl1: TODO
        :param st2: TODO
        :param sl2: TODO
        :param geometrical_set: geometrical set
        :type geometrical_set: :py:class:`~collectionsObject.hybridBodiesF.hybridBodies.HybridBody`
        :return: Line created
        :rtype: :class:`~Rice.abstractObjects.hybridShapes.line.LinePtPt`
        """
        if geometrical_set:
            geom = geometrical_set
        else:
            self.geometrical_set()
            geom = self.get_geometrical_set()[0]
        start  = self.point3D(start, st1, sl1)
        end = self.point3D(end, st2, sl2)
        line = self.factory.hybrid_shape_factory().AddNewLinePtPt(geom, start, end)
        return line

    def point3D(self, obj,st=None, sl=None, geometrical_set=None):
        """
        Create a 3D point from its coordinates.

        :param obj: coords of point
        :type obj: list of float or :class:`~Rice.abstractObjects.hybridShapes.point.PointCoord`
        :param st: TODO
        :param sl: TODO
        :param geometrical_set: geometrical set used
        :type geometrical_set: :class:`~Rice.collectionsObject.hybridBodies.HybridBody`
        :return: Point created
        :rtype: :class:`~Rice.abstractObjects.hybridShapes.point.PointCoord`
        """
        if geometrical_set:
            geom = geometrical_set
        else:
            self.geometrical_set()
            geom = self.get_geometrical_set()[0]
        if isinstance(obj, list):
            result = [obj, None]
        else:
            result = [None, self._createReferenceFromBRepName(obj, st, sl)]
        point = self.factory.hybrid_shape_factory().AddNewPointCoord(geom, *result)
        return point

    def fill(self, objs, geometrical_set=None):
        """
        Catia`s fill operation. Create a surface between objects.

        :param objs: objects to fill.
        :type objs: list of (:class:`~Rice.generalObjects.sketch.Sketch` or :class:`~Rice.abstractObjects.hybridShape.HybridShape`)
        :param geometrical_set: geometrical set used
        :type geometrical_set: :class:`~Rice.collectionsObject.hybridBodies.HybridBody`
        :return: Created surface
        :rtype: :class:`~Rice.abstractObjects.hybridShapes.fill.Fill`
        """
        if geometrical_set:
            geom = geometrical_set
        else:
            self.geometrical_set()
            geom = self.get_geometrical_set()[0]

        fill = self.factory.hybrid_shape_factory().AddNewFill(geom, objs)
        return fill

    def join(self, objs, geometrical_set=None):
        """
        Catia's join operation

        :param objs: objs to join
        :type objs: list of :class:`~Rice.abstractObjects.hybridShape.HybridShape`
        :param geometrical_set: geometrical set used
        :type geometrical_set: :class:`~Rice.collectionsObject.hybridBodies.HybridBody`
        :return: Joined surface
        :rtype: :class:`~Rice.abstractObjects.hybridShapes.join.Join`
        """
        if geometrical_set:
            geom = geometrical_set
        else:
            self.geometrical_set()
            geom = self.get_geometrical_set()[0]

        join = self.factory.hybrid_shape_factory().AddNewJoin(geom, objs)
        return join

    def spline(self, points, geometrical_set=None):
        """
        Catia's spline 3D operation.

        :param points: list of points
        :type points: list of (list of(int or float or :class:`~Rice.abstractObjects.hybridShapes.point.PointCoord`))
        :param geometrical_set: geometrical set used
        :type geometrical_set: :class:`~Rice.collectionsObject.hybridBodies.HybridBody`
        :return: Spline created
        :rtype: :class:`~Rice.abstractObjects.hybridShapes.spline.Spline`
        """
        if geometrical_set:
            geom = geometrical_set
        else:
            self.geometrical_set()
            geom = self.get_geometrical_set()[0]
        references = list()
        for i in points:
            if isinstance(i, list):
                references.append(self.point3D(i))
            else:
                references.append(i)
        spline = self.factory.hybrid_shape_factory().AddNewSpline(geom, references)
        return spline

    def _createReferenceFromBRepName(self, obj, param1, param2):
        """
            Only implemented for spline's Vertex
            param1 = 2 if obj is spline's first point
                     3 if obj is spline's last point
            param2 = +1 if obj is spline's first point
                     -1 if obj is spline's last point
        :param obj:
        :return:
        """
        sketch1 = obj.parent
        reference1 = self.cat_constructor.CreateReferenceFromBRepName(
            "BorderFVertex:(BEdge:(Brp:({};{});None:(Limits1:();Limits2:();{});Cf11:());WithPermanentBody;WithoutBuildError;WithSelectingFeatureSupport;MFBRepVersion_CXR15)".format(
                sketch1.name, param1, param2), sketch1.cat_constructor)
        return reference1

    def _createReferenceFromObject(self, obj):
        """
        :param obj:
        :return:
        """
        reference1 = self.cat_constructor.CreateReferenceFromObject(obj.cat_constructor)
        return reference1

    def create_param(self, param_type, name, value):
        """

        :param param_type: real, ....
        :type param_type: str
        :param name: Parameter's name
        :type name: str
        :param value: value of parameter
        :type value: float
        :return: Created parameter
        :rtype: :class:`~Rice.generalObjects.parameter.Parameter`
        """
        try: self.param_coll
        except: self.param_coll = Parameters(self.parentsDict._copy())

        obj = self.param_coll.__getattribute__('create_{}'.format(param_type))(name, value)
        return obj

    def create_formula(self, name, output, formula, comment=""):
        """

        :param name: Formula's name
        :type name: str
        :param output: Parameter object of the formula
        :type output: str
        :param formula: Expression
        :type formula: str
        :param comment:
        :return: formula created
        :rtype: :class:`~Rice.generalObjects.relation.Relation`
        """
        try: self.relations_coll
        except: self.relations_coll = Relations(self.parentsDict._copy())

        obj = self.relations_coll.create_formula(name, output, formula, comment)

        return obj

    def update(self):
        """
        Update part
        """
        self.cat_constructor.Update()
