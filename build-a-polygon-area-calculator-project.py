class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return_str = f"Rectangle(width={self.width}, height={self.height})"
        return return_str

    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter
    
    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal

    def get_picture(self):
        #Check that the dimensions of square or rectangle are not greater than 50
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        else:
            pict_str = ''
            for i in range(self.height):
                pict_line = ('*' * self.width) + '\n'
                pict_str += pict_line
            
            return pict_str
        

    def get_amount_inside(self, shape_obj):
        #To determine how many of the shape_obj for example a 2x2 square can fit inside the original object area
        #for example an 8x4 rectangle I used floor division of area. 
        return (self.get_area() // shape_obj.get_area())
        

class Square(Rectangle):
    def __init__(self, side):
        self.height = side
        self.width = side
    
    def __str__(self):
        return f"Square(side={self.height})"

    def set_side(self, side):
        self.height = side
        self.width = side

    #I override the set_width and set_height methods to make height and width the same given a value for width or height
    #Maybe there's a better way to do this?
    def set_width(self, width):
        self.height = width
        self.width = width

    def set_height(self, height):
        self.height = height
        self.width = height

rect_test = Rectangle(10,5)
print(rect_test.get_area())
rect_test.set_height(3)
print(rect_test.get_perimeter())
print(rect_test)
print(rect_test.get_picture())
print("\n")

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
sq.set_height(2)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

print(Rectangle(15,10).get_amount_inside(Square(5)))
