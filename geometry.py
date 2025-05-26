from math import sqrt

class Geometry:
    def __init__(self,point1,point2):
        self.a1,self.b1=point1
        self.a2,self.b2=point2

    def __str__(self):
        return f"point1 ({self.a1,self.b1}) and point2 ({self.a2,self.b2})"

    def distance(self,point1,point2):
        a1,b1=point1
        a2,b2=point2
        dist=sqrt((a2-a1)**2+(b2-b1)**2)
        return dist
    
    def middle(self):
        print(f"Middle point ({(self.a1+self.a2)/2},{(self.b1+self.b2)/2})")

    def trianglePerimeter(self):
        self.a3,self.b3=list(map(int,input("enter space separated cordinate: ").split()))
        self.a=self.distance((self.a1,self.b1),(self.a2,self.b2))
        self.b=self.distance((self.a2,self.b2),(self.a3,self.b3))
        self.c=self.distance((self.a3,self.b3),(self.a1,self.b1))

        print(f"Perimeter of traingle is:{self.a+self.b+self.c}")


    def triangleIsoscel(self):
        if self.a!=self.b and self.b!=self.c and self.a !=self.c:
            return False
        elif self.a==self.b and self.b==self.c and self.c==self.a:
            return False
        
        return True
    

obj=Geometry((1,1),(2,2))
print(obj.distance((1,1),(2,2)))
obj.middle()
obj.trianglePerimeter()
print(obj.triangleIsoscel())