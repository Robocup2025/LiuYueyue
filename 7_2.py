import random
import shutil
import string

def ori_file(line_num,line_length):
    x=string.printable
    f=open('test.txt','w')
    for i in range(line_num):
        line = ''.join(random.choice(x) for j in range(line_length))
        f.write(line+'\n')

def copy_file(ori_file_name,copy_file_name):
    shutil.copy(ori_file_name,copy_file_name)

if __name__ == '__main__':
    num=int(input())
    ori_file(num,10)
    copy_file('test.txt','copy_test.txt')