

import numpy

__author__ = 'roberto'


def rad_degrees(type_to, value):
    if type_to == 'rad':
        value = value*numpy.pi/180
    if type_to == 'deg':
        value = value*180/numpy.pi
    return value