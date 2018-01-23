import math
class point():
    """Represents a point in 2D space"""
pointa = point() #creates an instance of the class point's object
pointa.x = 1.0
pointa.y = 1.0

pointb = point() #creates the second instance of the class point's object
pointb.x = 3.0
pointb.y = 3.0

def distance_between_points(p1,p2):
    dis = ((p2.x - p1.x)**2) + ((p2.y - p1.y)**2)
    ans = math.sqrt(dis)
    return ans

print (distance_between_points(pointa,pointb))


