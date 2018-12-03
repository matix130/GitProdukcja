class Vector:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return f"Wektor ({self.x}, {self.y})"

    def __add__(self, other):
        nowy_x = self.x + other.x
        nowy_y = self.y + other.y
        return Vector(nowy_x, nowy_y)

    def __sub__(self, other):
        return Vector(self.x-other.x, self.y-other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x*other.x + self.y*other.y
        else:
            return Vector(self.x*other, self.y*other)
    def __truediv__(self, other):
        return self.x / other.x + self.y / other.y
    def __lt__(self, other):
        d1=(self.x ** 2 + self.y ** 2) ** (1/2)
        d2=(other.x ** 2 + other.y **2) ** (1/2)
        return d1<d2


v1=Vector(1, 3)
v2=Vector(2, 2)

print(v1)
print(v2)
v3=v1 + v2
print(v3)
v4 = v1.__add__(v2)
print(v4)
print("-"*30)
print(v1.__sub__(v2))
print("-"*30)
print(v1.__mul__(v2))

print(v1.__truediv__(v2))

print(v3*(v1/v2))