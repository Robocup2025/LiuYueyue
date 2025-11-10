x=int(input("x="))
f=[]
y=1
while x//10!=0:
    f.append(x%10)
    x=x//10
    y=y+1
f.append(x)
print(y)
for i in f:
    print(i,end=' ')