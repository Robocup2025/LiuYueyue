def f():
    with open('test.txt','r')as file:
        x=file.read()
    new_x=('python\n'+x+'\npython')
    with open('test.txt','w')as file:
        file.write(new_x)

if __name__=='__main__':
    f()