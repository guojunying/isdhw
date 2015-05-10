class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height

class Square(Rectangle):

    def __init__(self, width):
        self.width  = width
        self.height = width

class Circle(Rectangle):
	
	def __init__(self,r):
		self.r=width
		self.height=3.14*width
	
class Ellipse(Rectangle):
	
	def __init__(self,m,n):
		self.m=width
		self.n=3.14*height
	

def compute_area(shapes):
	shapes=[Ellipse(10,20),Square(15),Circle(5),Rectangle(20,15),Circle(5),Square(15),Ellipse(10,20)]
	sum(shapes)
def total_area: 
    total_area=compute_area(shapes)
    print(total_area)
