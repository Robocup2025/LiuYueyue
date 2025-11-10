def compare_file(file1,file2):
    with open(file1,'r') as f1:
        lines_one=f1.readlines()
    with open(file2,'r') as f2:
        lines_two=f2.readlines()
    length=min(len(lines_one),len(lines_two))
    for i in range(length):
        if lines_one[i]!=lines_two[i]:
            print(f"第{i+1}行不同")
            print(f"{file1}:{lines_one[i]}")
            print(f"{file2}:{lines_two[i]}")
    if len(lines_one)>len(lines_two):
        for i in range(len(lines_one)-len(lines_two)):
            l=len(lines_two)+i
            print(f"{file1}行数多于{file2}")
            print(f"{file1}:{lines_one[l]}")
    elif len(lines_two)>len(lines_one):
        for i in range(len(lines_two)-len(lines_one)):
            l = len(lines_one) + i
            print(f"{file2}行数多于{file1}")
            print(f"{file2}:{lines_two[l]}")

if __name__ == '__main__':
    compare_file('test.txt','copy_test.txt')