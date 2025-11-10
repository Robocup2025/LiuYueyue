a=0
b=1
f=[a,b]
for i in range(2,20):
    x=a+b
    a=b
    b=x
    f.append(x)
for i in f:
    print(i,end=' ')