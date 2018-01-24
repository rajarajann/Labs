class point:
    """this is a point class"""
    def __init__(self,x,y):
        """constructor for point"""
        self.x = x
        self.y = y
    def __str__(self):
        return ("The point is" + str (self.x) + "," + str (self.y))
    def __add__(self,other):
        my_point = point (self.x+other.x,self.y+other.y)
        return (my_point)


p1 = point (5,2)
p2 = point (10,10)
p3 = p1 + p2
p4 = p3 + p1
print (p4)



