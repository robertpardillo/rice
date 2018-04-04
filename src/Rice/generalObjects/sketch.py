from ..generalObjects.factory import Factory
from ..abstractObjects.hybridShapes.plane import Plane
from ..miscellaneous.tools import rad_degrees
from ..miscellaneous.orderDict import OrderDict
import numpy as np
from collections import namedtuple
from math import sqrt
from ..collectionsObject.constraints import Constraints


def Open_Close(func):
    def f(*args,**kwargs):
        self = args[0]
        self._open_edition()
        try: self.factory2d
        except: self.factory2D()
        obj = func(*args, **kwargs)
        self._close_edition()
        self.parentsDict['Part'].update()
        return obj
    return f


class Sketch(object):
    def __init__(self, parent, *args):
        self.parent = parent[parent[-1]]
        self.parentsDict = parent
        if not isinstance(args[0], Plane):
            self.cat_constructor = self.parent.cat_constructor.Add(args[0])
        else:
            self.cat_constructor = self.parent.cat_constructor.Add(args[0].cat_constructor)
        self.parentsDict[self.name] = self
        self._children = OrderDict()
        self.constraints_coll = Constraints(self.parentsDict._copy())

    def factory2D(self):
        self.factory2d = Factory(self.parentsDict).factory2d()

    def _add_children(self, obj):
        pass

    def _close_edition(self):
        self.cat_constructor.CloseEdition()
        #self.parentsDict['Part'].update()

    def _open_edition(self):
        self.cat_constructor.OpenEdition()

    @Open_Close
    def set_constraint(self, cstType, *references):
        """
        "catCstTypeReference":0,
        "catCstTypeDistance":1,
        "catCstTypeOn":2,
        "catCstTypeConcentricity":3,
        "catCstTypeTangency":4,
        "catCstTypeLength":5,
        "catCstTypeAngle":6,
        "catCstTypePlanarAngle":7,
        "catCstTypeParallelism":8,
        "catCstTypeAxisParallelism":9,
        "catCstTypeHorizontality":10,
        "catCstTypePerpendicularity":11,
        "catCstTypeAxisPerpendicularity":12,
        "catCstTypeVerticality":13,
        "catCstTypeRadius":14,
        "catCstTypeSymmetry":15,
        "catCstTypeMidPoint":16,
        "catCstTypeEquidistance":17,
        "catCstTypeMajorRadius":18,
        "catCstTypeMinorRadius":19,
        "catCstTypeSurfContact":20,
        "catCstTypeLinContact":21,
        "catCstTypePoncContact":22,
        "catCstTypeChamfer":23,
        "catCstTypeChamferPerpend":24,
        "catCstTypeAnnulContact":25,
        "catCstTypeCylinderRadius":26,
        "catCstTypeStContinuity":27,
        "catCstTypeStDistance":28,
        "catCstTypeSdContinuity":29,
        "catCstTypeSdShape":30
        :param cstType: Constraint Type
        :type cstType: int
        :param references:
        :return: Created Constraint
        :rtype: :class:`~Rice.generalObjects.constraint.Constraint`
        """
        if len(references)==1:
            const = self.constraints_coll.AddMonoEltCst(cstType, references[0])
        elif len(references)==2:
            const = self.constraints_coll.AddBiEltCst(cstType, *references)
        elif len(references) == 3:
            const = self.constraints_coll.AddTriEltCst(cstType, *references)
        else:
            raise AttributeError('"references" must have 1,2 or 3 elements')
        return const

    @Open_Close
    def remove_constraint(self, const):
        self.constraints_coll.remove(const)

    @property
    def name(self):
        return self.cat_constructor.Name

    @name.setter
    def name(self, value):
        self.cat_constructor.Name = value

    @Open_Close
    def arc(self, center, r, start, end, angle='deg'):
        """

        :param center: arc's center, [float, float]
        :type center: list of float
        :param r: radius of arc
        :type r: float
        :param start: starting angle
        :type start: float
        :param end: ending angle
        :type end: float
        :param angle: measuring units of angles
        :type angle: str
        :return: Created Arc
        :rtype: :class:`~Rice.abstractObjects.geometric2Delements.circle2D.Circle2D`
        """
        if angle == 'deg':
            start = rad_degrees('rad', start)
            end = rad_degrees('rad', end)
        circle = self.factory2d.AddArc(center, r, start, end)

        return circle

    @Open_Close
    def circle(self, center, r):
        """

        :param center: arc's center, [float, float]
        :type center: list of float
        :param r: radius of arc
        :type r: float
        :return: Created Circle
        :rtype: :class:`~Rice.abstractObjects.geometric2Delements.circle2D.Circle2D`
        """

        circle = self.factory2d.AddCircle(center, r)

        return circle

    @Open_Close
    def line2D(self, start, end, paint_start=True, paint_end=True):
        """

        :param start: [float, float] coordinates of starting point
        :type start: list of float
        :param end: [float, float] coordinates of starting point
        :type end: list of float
        :param paint_start: Do you want paint the starting point?
        :type paint_start: bool
        :param paint_end:Do you want paint the ending point?
        :type paint_end: bool
        :return: Created Line
        :rtype: :class:`~Rice.abstractObjects.geometric2Delements.line2D.Line2D`
        """

        line = self.factory2d.AddLine(start, end)

        if paint_start:
            line.start_point()
        if paint_end:
            line.end_point()

        return line

    @Open_Close
    def point2D(self, xc, yc):
        """

        :param xc: x coordinate
        :type xc: float
        :param yc: y coordinate
        :type yc: float
        :return: Created point
        :rtype: :class:`~Rice.abstractObjects.geometric2Delements.point2D.Point2D`
        """

        point = self.factory2d.AddPoint(xc, yc)

        return point

    def close_path(self, points):
        """
        Creates a closed path of points
        :param points: list of points [[float, float], [float, float], ...]
        :type points: list of (list of float)
        :return: list of lines
        :rtype: list of :class:`~Rice.abstractObjects.geometric2Delements.line2D.Line2D`
        """
        line_list = list()
        start = points[0]
        for i in range(len(points)-1):
            line = self.line2D(start, points[i+1], paint_start=True, paint_end=True)
            start = line.end
            line_list.append(line)
        else:
            line = self.line2D(start, line_list[0].start, paint_start=True, paint_end=True)
            line_list.append(line)

        return line_list

    @Open_Close
    def spline2D(self, points):
        """

        :param points: list of points
        :type points: list of (list of float or :class:`~Rice.abstractObjects.geometric2Delements.point2D.Point2D`)
        :return: Created Spline
        :rtype: :class:`~Rice.abstractObjects.geometric2Delements.spline2D.Spline2D`
        """

        spline = self.factory2d.AddSpline(points)

        return spline

    def arc_by_points(self, point1, point2, r, solution):
        """
        Create a circle arc that pass through two points
        :param point1: coordinates of one point
        :type point1: list of float
        :param point2: coordinates of another point
        :type point2: list of float
        :param r: radius
        :type r: float
        :param solution: 0 or 1
        :return: Created circle
        :rtype: :class:`~Rice.abstractObjects.geometric2Delements.circle2D.Circle2D`
        """

        Pt = namedtuple('Pt', 'x, y')
        Circle = Cir = namedtuple('Circle', 'x, y, r')
        def circles_from_p1p2r(p1, p2, r):
            'Following explanation at http://mathforum.org/library/drmath/view/53027.html'
            if r == 0.0:
                raise ValueError('radius of zero')
            (x1, y1), (x2, y2) = p1, p2
            if p1 == p2:
                raise ValueError('coincident points gives infinite number of Circles')
            # delta x, delta y between points
            dx, dy = x2 - x1, y2 - y1
            # dist between points
            q = sqrt(dx**2 + dy**2)
            if q > 2.0*r:
                raise ValueError('separation of points > diameter')
            # halfway point
            x3, y3 = (x1+x2)/2, (y1+y2)/2
            # distance along the mirror line
            d = sqrt(r**2-(q/2)**2)
            # One answer
            c1 = Cir(x = x3 - d*dy/q,
                     y = y3 + d*dx/q,
                     r = abs(r))
            # The other answer
            c2 = Cir(x = x3 + d*dy/q,
                     y = y3 - d*dx/q,
                     r = abs(r))
            return c1, c2

        result = circles_from_p1p2r(point1, point2, r)
        alpha1 = np.arctan2((point1[1]-result[0].y),(point1[0]-result[solution].x))
        alpha2 = np.arctan2((point2[1]-result[0].y),(point2[0]-result[solution].x))

        circle = self.arc([result[0].x,result[0].y], r,alpha1, alpha2, angle='rad')
        return circle
