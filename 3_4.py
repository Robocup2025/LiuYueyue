x=int(input("x="))
f=[]
z=x
y=1
k=0
while x//10!=0:
    f.append(x%10)
    x=x//10
    y=y+1
f.append(x)
for i in f:
    if f[i-1]!=f[y-i]:
        k=1
        break
if k==1:
    print(f"{z}不是回文数")
else:
    print(f"{z}是回文数")
