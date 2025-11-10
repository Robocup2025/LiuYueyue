x=int(input("x="))
y=int(input("y="))
z=int(input("z="))
if y>z:
    y,z=z,y
if x>y:
    x,y=y,x
if y>z:
    y,z=z,y
print(x,y,z)