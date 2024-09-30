class Coordinate(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2

        return (x_diff_sq + y_diff_sq)**0.5
    

c = Coordinate(3,4)
zero = Coordinate(0,0)

# instance call its method
print(c.distance(zero))

# pass both instances to the class
print(Coordinate.distance(c,zero))
