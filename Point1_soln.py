from __future__ import print_function, division

import copy
import math 

from Point1 import Point, Rectangle

def distance_between_points(p1, p2):
  """Computes the distance between two point objects.
  
  p1: Point
  p2: Point
  
  returns: float
  """
  
  dx = p1.x - p2.x
  dy = p1.y - p2.x
  dist = math.sqrt(dx**2 + dy**2)
  return dist


def move_rectangle(rect, dx,dy):
"""Move the rectangle by modifying itd corner objects.

rect: Rectangle object.
dx: change in x coordinates (can be negative)
dy: change in y coordinates (can be negative)
"""
rect.corner.x += dx
rect.corner.y += dy


def move_rectangle_copy(rect, dx, dy):
"""Move the Rectangle and retrun a new rectangle object.

rect: Rectangle object
dx: change in x coordinates (can be negative).
dy: change in y coordinates (can be negative).

returns: new rectangle
"""
new = copy.deepcopy(rec)
move_rectangle(new, dx, dy)
return new
