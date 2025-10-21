# -*- coding: utf-8 -*-
"""
Libreria di supporto alle lezioni del corso di Programmazione 1 al dipartimento di matematica
dell'Università di Pavia.

SOURCES: 
    
    1. La libreria svgpath2mpl (appare nella seconda meta di questo file)
       e` stata presa da questa repository:
          https://github.com/nvictus/svgpath2mpl

    2. La classe Tile e` stata ripresa e riadatta da questo sito:
          https://github.com/mapio/programming-with-escher/blob/master/notebook.ipynb
                  
Per le licenze d'uso, controllare i rispettivi siti
"""

from __future__ import division, print_function

from math import sqrt

import re
import numpy as np

from matplotlib import rcParams, pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch, Rectangle, Arc
from matplotlib.transforms import Affine2D as T

"""
SVGPATH2MPL
~~~~~~~~~~~
Parse SVG path data strings into matplotlib `Path` objects.

A path in SVG is defined by a 'path' element which contains a
``d="(path data)"`` attribute that contains moveto, line, curve (both
cubic and quadratic Béziers), arc and closepath instructions. See the SVG
Path specification at <https://www.w3.org/TR/SVG/paths.html>.

:copyright: (c) 2016, Nezar Abdennur.
:license: BSD.

"""
__version__ = '0.1.0'
__all__ = ['parse_path', 'EndpointArc']


COMMAND_RE = re.compile(r"([MLHVCSQTAZ])([^MLHVCSQTAZ]*)", re.IGNORECASE)
FLOAT_RE = re.compile(r"[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?")
COMMANDS = {
    'M' : (Path.MOVETO,),    # moveto
    'L' : (Path.LINETO,),    # line
    'H' : (Path.LINETO,),    # shorthand for horizontal line
    'V' : (Path.LINETO,),    # shorthand for vertical line
    'Q' : (Path.CURVE3,)*2,  # quadratic bezier
    'T' : (Path.CURVE3,)*2,  # shorthand for smooth quadratic bezier
    'C' : (Path.CURVE4,)*3,  # cubic bezier
    'S' : (Path.CURVE4,)*3,  # shorthand for smooth cubic bezier
    'Z' : (Path.CLOSEPOLY,), # closepath
    'A' : None               # arc
}
PARAMS = {
    'M' : 2, # moveto
    'L' : 2, # line
    'H' : 1, # shorthand for horizontal line
    'V' : 1, # shorthand for vertical line
    'Q' : 4, # quadratic bezier
    'T' : 4, # shorthand for smooth quadratic bezier
    'C' : 6, # cubic bezier
    'S' : 6, # shorthand for smooth cubic bezier
    'Z' : 0, # closepath
    'A' : 7  # arc
}

class EndpointArc(Arc):
    """
    Compute the path of an elliptical arc specified using "endpoint"
    parameterization.

    Parameters
    ----------
    start : pair of numbers
        The starting point of the arc path.
    radius : pair of numbers
        The x and y-components of the arc radius.
    angle : number
        The angle in degrees.
    large : bool
        Whether to generate a large arc spanning > 180 degrees (True) or a
        small arc spanning <= 180 degrees (False).
    sweep : bool
        Whether the line joining the center to arc sweeps through increasing
        angles (True) or decreasing angles (False).
    end : pair of numbers
        The final point of the arc path.

    Notes
    -----
    We must translate the "endpoint" to "center" parameterization.
    See <http://www.w3.org/TR/SVG/implnote.html#ArcConversionEndpointToCenter>.
    See also <http://stackoverflow.com/questions/197649/how-to-calculate-
    center-of-a-ellipse-by-two-points-and-radius-sizes>.

    """
    def __init__(self, start, radius, angle, large, sweep, end, **kwargs):
        x1, y1 = start
        rx, ry = radius
        x2, y2 = end
        def find_angle(u, v):
            u, v = map(np.asarray, [u, v])
            c = np.dot(u, v) / np.linalg.norm(u) / np.linalg.norm(v)
            return np.arccos(np.clip(c, -1, 1))

        # Handle out-of-range parameters
        # http://www.w3.org/TR/SVG/implnote.html#ArcOutOfRangeParameters
        if rx == 0 or ry == 0:
            return Path([[x2, y2]], [Path.MOVETO])
        if rx < 0: rx = abs(rx)
        if ry < 0: ry = abs(ry)
        angle = angle % 360

        # Translate the origin to the midpoint of the line joining (x1,y1) and
        # (x2,y2) and rotate the x & y axes to align with the axes of the
        # ellipse
        # step 1: transform (x1, y1) to the new coordinate system
        phi_rad = angle * np.pi / 180
        x1p = np.cos(phi_rad)*(x1-x2)/2 + np.sin(phi_rad)*(y1-y2)/2
        y1p = -np.sin(phi_rad)*(x1-x2)/2 + np.cos(phi_rad)*(y1-y2)/2
        lambd = ( (x1p * x1p) / (rx * rx) ) + ( (y1p * y1p) / (ry * ry) )
        if lambd > 1:
            rx = np.sqrt(lambd) * rx
            ry = np.sqrt(lambd) * ry

        # step 2: find the center of the ellipse in the new coordinate system
        sign = -1 if large == sweep else 1
        a = ((rx*rx*ry*ry - rx*rx*y1p*y1p - ry*ry*x1p*x1p) /
             (rx*rx*y1p*y1p + ry*ry*x1p*x1p))
        cxp = sign * np.sqrt(a) * (rx*y1p / ry)
        cyp = sign * np.sqrt(a) * (-ry*x1p / rx)

        # step 3: transform (cx', cy') back to the original coordinate system
        cx = np.cos(phi_rad)*cxp - np.sin(phi_rad)*cyp + (x1+x2)/2
        cy = np.sin(phi_rad)*cxp + np.cos(phi_rad)*cyp + (y1+y2)/2

        # step 4: compute angles
        theta1 = find_angle(
            [1, 0],
            [(x1p - cxp)/rx, (y1p - cyp)/ry]) * 180/np.pi
        dt = find_angle(
            [(x1p-cxp)/rx,   (y1p-cyp)/ry],
            [(-x1p-cxp)/rx, (-y1p-cyp)/ry]) * 180/np.pi
        dt %= 360
        if not sweep and dt > 0:
            dt -= 360
        elif sweep and dt < 0:
            dt += 360
        theta2 = theta1 - dt

        # generate an arc using center parameterization
        super(EndpointArc, self).__init__(
            xy=(cx, cy),
            width=rx*2,
            height=ry*2,
            angle=angle,
            theta1=theta1,
            theta2=theta2)


def _tokenize_path(d):
    for command, args in COMMAND_RE.findall(d):
        values = [float(v) for v in FLOAT_RE.findall(args)]
        while values:
            params = PARAMS[command.upper()]
            consumed, values = values[:params], values[params:]
            yield command, consumed
            

def parse_path(d):
    """
    Parse a path definition string (i.e., path data or ``d`` attribute)
    defining a shape in SVG into a matplotlib path object for plotting.

    Parameters
    ----------
    d : str
        SVG path data string.

    Returns
    -------
    ``matplotlib.path.Path`` object.

    """
    all_verts = []
    all_codes = []
    current_point = np.array([0., 0.])
    last_verts = None
    last_command = None
    start_point = current_point

    for command, values in _tokenize_path(d):

        is_relative = command.islower()
        command = command.upper()

        if command == 'Z':
            # Close path. A point is required but ignored.
            verts = np.array(start_point)
            codes = COMMANDS[command]

        elif command == 'H':
            # Horizontal line.
            verts = np.r_[values, 0.]
            codes = COMMANDS[command]

        elif command == 'V':
            # Vertical line.
            verts = np.r_[0., values]
            codes = COMMANDS[command]

        elif command == 'T':
            # Smooth quadratic curve. If previous command was a Q/q or T/t,
            # the control point is the "reflection" of the second control point
            # in the previous segment.
            control_point = np.array([0., 0.])
            if last_command in ('Q', 'T'):
                x1, y1 = last_verts[-2]
                x2, y2 = current_point
                dx, dy = x2 - x1, y2 - y1
                control_point += [dx, dy]
            verts = np.r_[control_point, values]
            codes = COMMANDS[command]

        elif command == 'S':
            # Smooth cubic curve. If previous command was a C/c or S/s,
            # the control point is the "reflection" of the third control point
            # in the previous segment.
            control_point = np.array([0., 0.])
            if last_command in ('C', 'S'):
                x1, y1 = last_verts[-3]
                x2, y2 = current_point
                dx, dy = x2 - x1, y2 - y1
                control_point += [dx, dy]
            verts = np.r_[control_point, values]
            codes = COMMANDS[command]

        elif command == 'A':
            # Elliptical arc using endpoint parameterization.
            x1, y1 = 0., 0.
            rx, ry, phi, large, sweep, x2, y2 = values
            arc = EndpointArc((x1, y1), (rx, ry), phi, large, sweep, (x2, y2))
            arcpath = arc.get_path()
            # Get the right vertex coordinates
            verts = arc.get_patch_transform().transform(arcpath.vertices)
            codes = arcpath.codes
            # First command is a MOVETO, which would make a new subpath. Drop it.
            verts = verts[1:, :].ravel()
            codes = codes[1:].ravel()

        else:
            # M, L, Q, C
            verts = np.array(values)
            codes = COMMANDS[command]

        verts = verts.reshape(len(verts)//2, 2)

        if is_relative:
            verts += current_point

        last_verts = verts
        last_command = command
        current_point = verts[-1]
        all_verts.extend(verts.tolist())
        all_codes.extend(codes)

    return Path(all_verts, all_codes)


"""
----------------------------------------------------------------------------------
"""
__all__ = __all__ + ['blank', 'f', 'triangle', 'fish', 'edge', 'Tile',
                     'flip', 'rot', 'rot45', 'over', 'beside', 'above', 'setSize', ]

class Tile(object):
    
    def __init__(self, path = None):
        self.bbox = True
        if not path: path = Path([(0,0)])
        self.path = path
        self.fill = False
        self.color = 'black'

    @classmethod
    def read(cls, name):
        with open('{}.path'.format(name)) as _: 
            return cls(
                parse_path(_.read()).transformed(
                    T().scale(1, -1).translate(0, 1)
                )
            )

    @classmethod
    def parse(cls, p):
        return cls(
            parse_path(p).transformed(
                T().scale(1, -1).translate(0, 1)
            )
        )            

    @staticmethod
    def union(tile0, tile1):
        return Tile(Path.make_compound_path(tile0.path, tile1.path))
            
    @staticmethod
    def transform(tile, transform):
        return Tile(tile.path.transformed(transform))
            
    def _ipython_display_(self):
        fig, ax = plt.subplots()
        ax.add_patch(PathPatch(self.path, fill = False))
        if self.bbox:
            r = Rectangle((0,0), 1, 1, fill = False, linestyle = 'dotted')
            ax.add_patch(r)
        plt.axis('equal')
        plt.axis('off')
        return fig

def flip(tile):
    return Tile.transform(tile, T().scale(-1, 1).translate(1, 0))

def rot(tile):
    return Tile.transform(tile, T().rotate_deg(90).translate(1, 0))

def rot45(tile):
    return Tile.transform(tile,
        T().rotate_deg(45).scale(1 / sqrt(2), 1 / sqrt(2)).translate(1 / 2, 1 / 2)
    )

def over(tile0, tile1):
    return Tile.union(tile0, tile1)

def beside(tile0, tile1, n = 1, m = 1):
    den = n + m
    return Tile.union(
        Tile.transform(tile0, T().scale(n / den, 1)),
        Tile.transform(tile1, T().scale(m / den, 1).translate(n / den, 0))
    )

def above(tile0, tile1, n = 1, m = 1):
    den = n + m
    return Tile.union(
        Tile.transform(tile0, T().scale(1, n / den).translate(0, m / den)),
        Tile.transform(tile1, T().scale(1, m / den))
    )

def setSize(n):
    rcParams['figure.figsize'] = n, n

# Imposta un valore di default per la dimensione di una tile
setSize(5)

# Tile vuota
blank = Tile()

# Sequenza di comandi per disegnare un triangolo
# Leggere la documentazione delle 'SVG path':
#    https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths
TR = """ M 0.,1.
         L 1.,1.
         L 0.,0.
         L 0.,1. """

triangle = Tile.parse(TR)
    
# Sequenza di comandi per disegnare la lettera F in una 'tile'
F = """ M .1, .1
        L .9, .1
        L .9, .2
        L .2, .2
        L .2, .4
        L .6, .4
        L .6, .5
        L .2, .5
        L .2, .9
        L .1, .9
        L .1, .1 """

f = Tile.parse(F)

# Sequenza di comandi per generare un 'edge'
# Per capire come funzionano le curve di Bezier, vedi:
#    https://en.wikipedia.org/wiki/B%C3%A9zier_curve
EDGE = """  M 1.,1.
            C 0.78,0.95 0.78,0.95 0.58,0.97
            C 0.38,0.80 0.38,0.80 0.25,0.73
            L 0.,1. """
            
edge = Tile.parse(EDGE)

# Sequenza di comandi per generare il pesce di Escher
# File sorgente: 
FISH = """  M 0.00 0.00
            C 0.08 0.02 0.22 0.18 0.29 0.28
            M 0.30 0.50
            C 0.34 0.60 0.43 0.68 0.50 0.74
            M 0.50 0.74
            C 0.58 0.79 0.66 0.78 0.76 0.80
            M 0.76 0.80
            C 0.82 0.88 0.94 0.95 1.00 1.00
            M 1.00 1.00
            C 0.90 0.97 0.81 0.96 0.76 0.95
            M 0.76 0.95
            C 0.69 0.96 0.62 0.96 0.55 0.96
            M 0.55 0.96
            C 0.49 0.90 0.40 0.83 0.35 0.80
            M 0.35 0.80
            C 0.29 0.76 0.19 0.72 0.14 0.69
            M 0.14 0.69
            C 0.09 0.65 -0.03 0.57 -0.05 0.28
            M -0.05 0.28
            C -0.04 0.18 -0.02 0.05 0.00 0.00
            M 0.10 0.15
            C 0.14 0.18 0.18 0.22 0.18 0.25
            M 0.18 0.25
            C 0.16 0.26 0.14 0.27 0.12 0.27
            M 0.12 0.27
            C 0.11 0.23 0.11 0.19 0.10 0.15
            M 0.05 0.18
            C 0.10 0.20 0.08 0.26 0.09 0.30
            M 0.09 0.30
            C 0.07 0.32 0.06 0.34 0.04 0.33
            M 0.04 0.33
            C 0.04 0.27 0.04 0.19 0.05 0.18
            M 0.11 0.30
            C 0.16 0.44 0.24 0.61 0.30 0.66
            M 0.30 0.66
            C 0.41 0.78 0.62 0.84 0.80 0.92
            M 0.23 0.20
            C 0.35 0.20 0.44 0.22 0.50 0.25
            M 0.50 0.25
            C 0.50 0.33 0.50 0.41 0.50 0.49
            M 0.50 0.49
            C 0.46 0.53 0.42 0.57 0.38 0.61
            M 0.29 0.29
            C 0.36 0.26 0.43 0.27 0.48 0.31
            M 0.34 0.39
            C 0.38 0.34 0.44 0.36 0.48 0.37
            M 0.34 0.49
            C 0.38 0.44 0.41 0.42 0.48 0.43
            M 0.45 0.58
            C 0.46 0.60 0.47 0.61 0.48 0.61
            M 0.42 0.61 
            C 0.43 0.64 0.46 0.68 0.48 0.67
            M 0.25 0.74
            C 0.17 0.83 0.08 0.91 0.00 0.99
            M 0.00 0.99
            C -0.08 0.91 -0.17 0.82 -0.25 0.74
            M -0.25 0.74
            C -0.20 0.63 -0.11 0.53 -0.03 0.43
            M -0.17 0.74
            C -0.13 0.66 -0.08 0.60 -0.01 0.56
            M -0.12 0.79
            C -0.07 0.71 -0.02 0.66 0.05 0.60
            M -0.06 0.86
            C -0.03 0.77 0.03 0.72 0.10 0.66
            M -0.02 0.92
            C 0.02 0.84 0.09 0.77 0.16 0.70 """

fish = Tile.parse(FISH)