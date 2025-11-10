f=[1,2,3,4]
num=[]
for x in f:
    for y in f:
        for z in f:
            if (x!=y) and (x!=z) and (y!=z):
                a=100*x+10*y+z
                num.append(a)
print(f"能组成{len(num)}个互不相同且无重复数字的三位数")
print("分别为：")
for x in num:
    print(x)