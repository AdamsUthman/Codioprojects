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
