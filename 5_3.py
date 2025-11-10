import random

def f(length,min_num,max_num):
    f=open('data.txt','w')
    for i in range(length):
        x=random.randint(min_num,max_num)
        f.write(str(x)+'\n')
if __name__ == '__main__':
    f(100000,1,100)