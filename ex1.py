class Point:
    color = "red"
    circle = 2


a = Point()



Point.circle = 3

Point.type_pt = 'disc'

print(Point.__dict__)

setattr(Point, 'prop', 1)
setattr(a, 'color', 'black')

hasattr(Point, 'prop')
delattr(Point, 'prop')

print(Point.__dict__)

del a.color

a = Point()
b = Point()

a.x = 1
a.y = 2

b.x = 10
b.y = 20
