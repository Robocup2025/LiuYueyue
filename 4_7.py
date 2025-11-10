x=list(range(1,233))
y=0
while len(x)>1:
    y=(y+2)%len(x)
    x.pop(y)
print(x[0])