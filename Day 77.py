class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.k = j
        self.j = k
    
    def __str__(self):
        return f"{self.i}i + {self.k}k + {self.j}j"
    
    def __add__(self,x):
        return Vector(self.i + x.i, self.k + x.k, self.j + x.j)

#   + : __add__
#   - : __sub__
#   * : __mul__
#   / : __truediv__
#   < : __lt__
#   > : __gt__
#   == : __eq__


v1 = Vector(3,5,6)
print(v1)

v2 = Vector(1,6,8)
print(v1)

print(f"Total: {v1+v2}")
print(type(v1+v2))