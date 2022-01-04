class Rectangle:
    def __init__(self,x,y,width,height):
        # initializes the instance attributes of a Rectangle object
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def display(self):
        display_string = 'x = '+str(self.x)+',y = '+str(self.y)+',width = '+str(self.width)+',height = '+str(self.height)
        return display_string
    def left(self):
        return self.x
    def top(self):
        return self.y
    def right(self):
        return self.x + self.width
    def bottom(self):
        return self.y + self.height
    def collide_point(self,point):
        # - point is a tuple (x,y)
        # returns True if point is inside or on the border of the rectangle
        # False otherwise
        within_x_range = point[0] >= self.left() and point[0] <= self.right()
        within_y_range = point[1] >= self.top() and point[1] <= self.bottom()
        
        # if within_x_range and within_y_range:
            # return True
        # else:
            # return False
        return within_x_range and within_y_range
    def collide_rectangle(self,other):
        # - other is a Rectangle object
        # return True if rectangles overlap
        # returns False otherwise
        self_on_left = self.right() < other.left()
        self_on_right = self.left() > other.right()
        self_on_top = self.bottom() < other.top()
        self_on_bottom = self.top() > other.bottom()
        
        # if self_on_left or self_on_right or self_on_top or self_on_bottom:
        #     return False
        # else:
        #     return True        
        return not (self_on_left or self_on_right or self_on_top or self_on_bottom)
        
        
def main ():
    # main program
    red = Rectangle(25,50,50,25)
    print(red.display())
    green = Rectangle(100,100,25,50)
    print(green.display())
    point_a = (50,63)
    point_b = (113,125)
    print(red.collide_point(point_a)) # True
    print(green.collide_point(point_b)) # True
    blue = Rectangle(50,63,50,25)
    print(red.collide_rectangle(blue)) # True
    print(green.collide_rectangle(blue)) # False
    
main()