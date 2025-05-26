class rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b

    def perimeter(self):
        return 2*(self.length+self.breadth)
    
    def area(self):
        return self.length*self.breadth
    
    def display(self):
        print(f"Length:{self.length}\nBreadth:{self.breadth}\nPerimeter:{self.perimeter()}\nArea:{self.area()}")


class Parallelepipede(rectangle):
    def __init__(self,l,b,h):
        self.height=h
        super().__init__(l,b)

    def volume(self):
        return self.length*self.breadth*self.height
    


obj=Parallelepipede(10,20,10)
print(obj.perimeter())
print(obj.area())
print(obj.display())
print(obj.volume())